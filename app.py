import streamlit as st
import pandas as pd
import os

# Mobielvriendelijke instellingen
st.set_page_config(page_title="Container Zoeker", layout="centered")

st.title("🗑️ Container Data Zoeker")

# Bestandsnaam van de CSV die in dezelfde map staat
CSV_BESTAND = "WasteVision Vulsnelheid(wastecontainers vulstatus (2)).csv"

# Controleer of het bestand aanwezig is
if os.path.exists(CSV_BESTAND):
    # Lees de CSV automatisch in
    df = pd.read_csv(CSV_BESTAND, sep=";")
    
    # Zorg dat de kolom 'Number' als tekst wordt gezien voor het zoeken
    df['Number'] = df['Number'].astype(str)

    # 1. Inputveld voor het specifieke nummer
    # Met 'autocomplete' uitgeschakeld voor een fijnere mobiele ervaring
    zoek_nummer = st.text_input("Typ het containernummer (Number):", autocomplete="off")

    if zoek_nummer:
        # Zoek naar overeenkomst in de 'Number' kolom
        resultaten = df[df['Number'].str.contains(zoek_nummer, case=False, na=False)]

        # 2. Toon de specifieke kolommen
        st.subheader(f"Resultaten ({len(resultaten)} gevonden):")
        
        if not resultaten.empty:
            for index, row in resultaten.iterrows():
                # Overzichtelijke kaartjes voor op je mobiel
                with st.container():
                    st.markdown(f"### 📍 Container {row['Number']}")
                    st.write(f"**Name:** {row['Name']}")
                    st.write(f"**Sub area:** {row['Sub area']}")
                    st.write(f"**Fills in (days):** {row['Fills in (days)']}")
                    st.markdown("---")
        else:
            st.warning(f"Geen container gevonden met nummer '{zoek_nummer}'.")
    else:
        st.info("Typ hierboven een nummer om te zoeken.")
else:
    st.error(f"Bestand niet gevonden! Zorg dat '{CSV_BESTAND}' in dezelfde map staat als app.py.")