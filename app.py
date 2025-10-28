import streamlit as st
from palette_generator import generate_palette

st.set_page_config(page_title="AI Color Palette Generator", page_icon="🎨")

st.title("🎨 AI Color Palette Generator")
st.write("Bir kelime yaz, yapay zekâ sana ilham veren bir renk paleti oluştursun!")

keyword = st.text_input("Kelime girin", "")

if st.button("Paleti Oluştur") and keyword:
    with st.spinner("Renkler oluşturuluyor..."):
        palette = generate_palette(keyword)
        st.success("Palet oluşturuldu!")

        cols = st.columns(len(palette))
        for i, color in enumerate(palette):
            with cols[i]:
                st.color_picker(f"Renk {i+1}", color, label_visibility="collapsed")
                st.write(color)