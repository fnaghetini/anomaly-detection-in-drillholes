import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_category_frequencies(df: pd.DataFrame(), categ_feature: str) -> None:
    labels = df[categ_feature].value_counts().sort_values().index
    values = df[categ_feature].value_counts().sort_values().values
    plt.figure(figsize=(8, 8))
    p = sns.countplot(y=categ_feature, data=df, color='steelblue', edgecolor='black', order=labels)
    for i, v in enumerate(values):
        p.text(v + 30, i, str(v), va='center', size=12)
    plt.xlabel("Frequência absoluta", size=12)
    plt.xticks(np.arange(0, 7_500, 500))
    plt.ylabel("")


def plot_boxplots_by_litho(df: pd.DataFrame(), numeric_features: list, categ_feature: str) -> None:
    n = len(numeric_features)
    fig, axs = plt.subplots(n, 1, figsize=(6, n * 2))

    for ax, f in zip(axs, numeric_features):
        sns.boxplot(y=f, x=categ_feature, data=df, ax=ax)
        if f != numeric_features[n - 1]:
            ax.axes.get_xaxis().set_visible(False)


def plot_correlation_heatmap(df: pd.DataFrame(), features: list, corr_filter=0) -> None:
    correlation_matrix = df[features].corr()
    lower_triangle_mask = (np.triu(np.ones_like(correlation_matrix, dtype=bool)))
    corr_value_mask = (np.abs(correlation_matrix) <= corr_filter)

    plt.figure(figsize=(13, 11))
    ax = sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap='coolwarm',
        cbar=True,
        mask=lower_triangle_mask | corr_value_mask,
        square=True,
        linewidths=0.5,
        fmt='.2f',
        vmin=-1.0, vmax=1.0
    )
    ax.set_xticklabels(features, rotation=45)
    ax.set_yticklabels(features, rotation=0)
    plt.show()


def plot_explained_variance_for_pcs(pca):
    explained_var = (pca.explained_variance_ratio_ * 100).round(3)
    cum_explained_var = np.cumsum(explained_var).round(2)
    pc_names = ['PC' + str(i) for i in range(1, len(explained_var) + 1)]

    fig, ax1 = plt.subplots(figsize=(7, 3))

    ax1.bar(x=pc_names, height=explained_var, color='steelblue', edgecolor='black')
    ax1.set_ylabel("Variância explicada relativa (%)", size=10)

    ax2 = ax1.twinx()
    ax2.plot(pc_names, cum_explained_var, color='black', marker='o', lw=1)
    ax2.set_ylabel('Variância explicada acumulada (%)', size=10)
    ax2.set_yticks(np.arange(0, 140, 20))

    for i, v in enumerate(cum_explained_var):
        ax2.text(i, v + 3, f"{v}%", ha='center', size=8)

    plt.tight_layout()
    plt.show()



def plot_pcs_colored_by_litho(principal_components, categorical_variable):
    unique_categories = np.unique(categorical_variable)
    colors = plt.cm.get_cmap('tab10', len(unique_categories))
    for i, category in enumerate(unique_categories):
        plt.scatter(principal_components[categorical_variable == category, 0],
                    principal_components[categorical_variable == category, 1],
                    color=colors(i), label=category, s=10, marker='+')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend(loc='best')
    plt.show()


def plot_model_pred_by_litho(df:pd.DataFrame(), litho: str):
    litho_mask = (df['LITHO'] == litho)
    inline_mask = ((df['ISF_PRED'] != -1) & (df['DBS_PRED'] != -1) & (df['LOF_PRED'] != -1))
    df_inline = df[litho_mask & inline_mask]
    plt.scatter(df_inline['PC1'], df_inline['PC2'], color='white', s=20, marker='o', label='Inliners', edgecolor='black', linewidth=1)
    plt.scatter(df[df['ISF_PRED'] == 1]['PC1'], df[df['ISF_PRED'] == 1]['PC2'], color='red', s=20, marker='o', label='ISF', edgecolor='black', linewidth=1)
    plt.scatter(df[df['DBS_PRED'] == 1]['PC1'], df[df['DBS_PRED'] == 1]['PC2'], color='green', s=20, marker='o', label='DBS', edgecolor='black', linewidth=1)
    plt.scatter(df[df['LOF_PRED'] == 1]['PC1'], df[df['LOF_PRED'] == 1]['PC2'], color='yellow', s=20, marker='o', label='LOF', edgecolor='black', linewidth=1)
    plt.title(f"Litologia: {litho}")
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend(loc='best')
    plt.show()


def plot_model_votes_by_litho(df:pd.DataFrame(), litho: str):
    litho_mask = (df['LITHO'] == litho)
    df = df[litho_mask]
    p = plt.scatter(df['PC1'], df['PC2'], c=df['VOTES'], s=20, marker='o', cmap='jet', edgecolor='white', linewidth=1)
    plt.title(f"Litologia: {litho}")
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    cb = plt.colorbar(p)
    cb.set_label('N° Votos', fontsize=12)
    plt.show()
