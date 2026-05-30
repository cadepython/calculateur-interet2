import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuration of the page

st.set_page_config(
    page_title="Calculateur d'Intérêt",
    page_icon="💰",
    layout="centered"
)


# Header

st.markdown(
    "<h5 style='text-align: left; color: gray;'>Programme créé par Caden</h5>",
    unsafe_allow_html=True
)

st.title("Calculateur d'Intérêt")

# Entrées

st.header("Données")

capital = st.number_input(
    "Capital Initial ($)",
    min_value=0.0,
    value=1000.0,
    step=1.0
)

taux = st.number_input(
    "Taux d'intérêt (%)",
    min_value=0.0,
    value=5.0,
    step=1.0
)

temps = st.number_input(
    "Temps (années)",
    min_value=1,
    value=10,
    step=1
)

frequence = st.number_input(
    "Nombre de compositions par année",
    min_value=1,
    value=1,
    step=1
)


# Button

if st.button("Calculer"):

    taux_decimal = taux / 100

    # INTÉRÊT SIMPLE

    st.divider()

    st.header("Intérêt Simple")

    st.latex(r"I = P \times r \times t")

    interet_simple = capital * taux_decimal * temps
    montant_simple = capital + interet_simple

    st.write("**1.**")
    st.code(f"I = {capital:.2f} × {taux_decimal:.2f} × {temps}")

    st.write("**2.**")
    st.code(f"I = {interet_simple:.2f}")

    st.write("**3.**")
    st.code(
        f"Montant Final = {capital:.2f} + {interet_simple:.2f}"
    )

    st.write("**4.**")
    st.code(f"Montant Final = {montant_simple:.2f}")

    st.success(
        f"Montant Final (Intérêt Simple) : ${montant_simple:.2f}"
    )

    # INTÉRÊT COMPOSÉ

    st.divider()

    st.header("Intérêt Composé")

    st.latex(r"A = P(1+\frac{r}{n})^{nt}")

    montant_compose = capital * (
        1 + taux_decimal / frequence
    ) ** (frequence * temps)

    st.write("**1.**")
    st.code(
        f"A = {capital:.2f}(1 + {taux_decimal:.2f}/{frequence})^({frequence}×{temps})"
    )

    st.write("**2.**")
    st.code(
        f"A = {capital:.2f}(1 + {taux_decimal / frequence:.4f})^({frequence * temps})"
    )

    st.write("**3.**")
    st.code(
        f"A = {capital:.2f} × {(1 + taux_decimal / frequence):.4f}^{frequence * temps}"
    )

    st.write("**4.**")
    st.code(f"A = {montant_compose:.2f}")

    st.success(
        f"Montant Final (Intérêt Composé) : ${montant_compose:.2f}"
    )

    # TABLEAU

    st.divider()

    st.header("Tableau")

    annees = []
    simple_values = []
    compose_values = []

    for annee in range(int(temps) + 1):

        simple = capital + (
            capital * taux_decimal * annee
        )

        compose = capital * (
            1 + taux_decimal / frequence
        ) ** (frequence * annee)

        annees.append(annee)
        simple_values.append(round(simple, 2))
        compose_values.append(round(compose, 2))

    df = pd.DataFrame({
        "Année": annees,
        "Simple ($)": simple_values,
        "Composé ($)": compose_values
    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # GRAPHIQUE

    st.divider()

    st.header("Graphique")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
        annees,
        simple_values,
        color="blue",
        linewidth=2,
        label="Intérêt Simple"
    )

    ax.plot(
        annees,
        compose_values,
        color="red",
        linewidth=2,
        label="Intérêt Composé"
    )

    ax.set_xlabel("Années")
    ax.set_ylabel("Montant ($)")
    ax.set_title("Comparaison des Intérêts")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)