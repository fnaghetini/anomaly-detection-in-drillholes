import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def pdp(df, features, yname, n=4, 
        writefolder=None, digits=2, figsize=(8,6), 
        showbincount=True, ylim_origin=True,
        even_spaced_ticks=False):
  
  assert isinstance(yname, str), 'yname must be a string. Unique column.'
  assert yname in df.columns, 'yname column is not in the dataframe.'
  assert isinstance(features, list), 'features must be a list. If single feature use [feature].'

  for feature in features:
    
    if feature != yname:

        if feature not in df.columns:
            print (f'feature {feature} not in df.')
            continue

        replace_list = ['/', '\\', ' ', '(', ')']

        feature_string = str(feature)
        for char in replace_list:
          feature_string = feature_string.replace(char, '_')

        yname_string = str(yname)
        for char in replace_list:
          yname_string = yname_string.replace(char, '_')

        # tirando os nans

        try:
          #df_temp = df[~np.isnan(df[feature])][[feature, yname]]
          df_temp = df[[feature, yname]].dropna()

          bins_pos = np.percentile(df_temp[feature].values, np.linspace(0,100,n+1))
        except:
          print ('feature {} with problems.'.format(feature))
          continue
        v_mean = list()
        v_std = list()

        if bins_pos.size == np.unique(bins_pos).size: # variavel continua
          hist, _ = np.histogram(df_temp[feature], bins_pos)
          xtickslabel = list()
          bin_pos_label = list()
          for i in range(bins_pos.size-1): # vou pegar cada intervalo agora e calcular a media de y
            v = df_temp[(df_temp[feature].values >= bins_pos[i]) & (df_temp[feature].values < bins_pos[i+1])][yname].values
            if np.isnan(v.mean()) or np.isnan(v.std()) or abs(v.mean())==float('inf') or abs(v.std())==float('inf'):
              continue
            else:
              xtickslabel.append('['+'{number:.{digits}f}'.format(number=bins_pos[i], digits=digits)+'-'+'{number:.{digits}f}'.format(number=bins_pos[i+1], digits=digits)+'[')
              v_mean.append(v.mean())
              v_std.append(v.std())
              if even_spaced_ticks:
                bin_pos_label.append((bins_pos[i]+bins_pos[i+1])/2)
              else:
                bin_pos_label.append(i)

          v_mean = np.array(v_mean)
          v_std = np.array(v_std)/np.sqrt(hist)

          fig, ax1 = plt.subplots(figsize=figsize)
          ax1.set_xlabel(feature)
          ax1.set_ylabel('mean ' + yname)
          ax1.set_ylim([(v_mean-v_std).min()*0.9, (v_mean+v_std).max()*1.05])
          ax1.set_xticks(bin_pos_label)
          #ax1.plot(bins_pos[:-1], v_mean, label='mean '+yname)
          ax1.plot(bin_pos_label, v_mean, 'o-', label='mean '+yname)
          ax1.set_xticklabels(xtickslabel, rotation=35)
          #ax1.fill_between(bins_pos[:-1], v_mean + v_std, v_mean - v_std, alpha=0.1, color='b')
          ax1.fill_between(bin_pos_label, v_mean + v_std, v_mean - v_std, alpha=0.1, color='b')

          if showbincount:
            color = 'tab:red'
            ax2 = ax1.twinx()
            ax2.plot(bin_pos_label, hist, 'o--', label='bin count', color=color)
            #ax2.bar(bin_pos_label, hist, label='bin count', color=color)
            ax2.set_ylim([0, hist.max()*1.2])
            ax2.set_ylabel('bin_count', color=color)

          if writefolder:
            feature_ = feature.replace(' ', '_')
            feature_ = feature_.replace('/', '_')
            plt.savefig(writefolder+'/scatter_feature_'+feature_string+'_y_'+yname_string+'.png')
          else:      
            plt.tight_layout()
            plt.show()
        else: # variavel categorica
          bins_pos = np.unique(bins_pos)
          hist = list()
          for value in bins_pos:
            hist.append((df_temp[feature].values==value).sum())
          #hist, _ = np.histogram(df[feature], bins_pos)
          for i in range(bins_pos.size): # vou pegar cada intervalo agora e calcular a media de y
            v = df_temp[df_temp[feature].values == bins_pos[i]][yname].values
            v_mean.append(v.mean())
            v_std.append(v.std())

          v_mean = np.array(v_mean)
          v_std = np.array(v_std)/np.sqrt(hist)

          fig, ax1 = plt.subplots(figsize=figsize)
          ax1.set_xlabel(feature)
          ax1.set_ylabel('mean '+yname)
          if ylim_origin:
            ax1.set_ylim([0,(v_mean+v_std).max()*1.05])
          else:
            ax1.set_ylim([(v_mean-v_std).min()*0.95,(v_mean+v_std).max()*1.05])
          ax1.set_xticks(bins_pos)
          ax1.plot(bins_pos, v_mean, 'o-', label='mean '+yname)
          ax1.fill_between(bins_pos, v_mean + v_std, v_mean - v_std, alpha=0.1, color='b')

          if showbincount:
            color = 'tab:red'
            ax2 = ax1.twinx()
            ax2.plot(bins_pos, hist, 'o--', label='bin count', color=color)
            ax2.set_ylim([0, np.array(hist).max()*1.2])
            ax2.set_ylabel('bin_count', color=color)

          if writefolder:
            plt.savefig(writefolder+'/pdp_feature_'+feature_string+'_y_'+yname_string+'.png')
          else:      
            plt.show()
