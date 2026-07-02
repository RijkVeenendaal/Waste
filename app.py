import streamlit as st
import pandas as pd

# Mobielvriendelijke instellingen
st.set_page_config(page_title="Container Zoeker", layout="centered")

st.title("🗑️ Container Data Zoeker")

# 1. Upload het CSV-bestand
uploaded_file = st.file_uploader("Kies het WasteVision CSV-bestand", type=["csv"])

if uploaded_file is not None:
    # Lees de CSV in (met ';' als scheidingsteken)
    df = pd.read_csv(uploaded_file, sep=";")
    
    # Zorg dat de kolom 'Number' als tekst wordt gezien voor het zoeken
    df['Number'] = df['Number'].astype(str)

    # 2. Inputveld voor het specifieke nummer
    zoek_nummer = st.text_input("Typ het containernummer (Number):")

    if zoek_nummer:
        # Zoek naar exacte of gedeeltelijke overeenkomst in de 'Number' kolom
        resultaten = df[df['Number'].str.contains(zoek_nummer, case=False, na=False)]

        # 3. Toon de specifieke kolommen
        st.subheader(f"Resultaten ({len(resultaten)} gevonden):")
        
        if not resultaten.empty:
            for index, row in resultaten.iterrows():
                # Toon de resultaten in een strak overzicht voor op de telefoon
                with st.container():
                    st.markdown(f"### 📍 Container {row['Number']}")
                    st.write(f"**Name:** {row['Name']}")
                    st.write(f"**Sub area:** {row['Sub area']}")
                    st.write(f"**Fills in (days):** {row['Fills in (days)']}")
                    st.markdown("---")
        else:
            st.warning(f"Geen container gevonden met nummer '{zoek_nummer}'.")
else:
    st.info("Upload het 'WasteVision Vulsnelheid' CSV-bestand om te beginnen.")