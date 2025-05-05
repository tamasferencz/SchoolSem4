from fpdf import FPDF  # FPDF importálása

# Létrehozzuk a PDF dokumentumot
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Betűtípus beállítása
pdf.set_font("Arial", size=12)

# Cím
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Érzékelés típusai – Tanulókártya PDF", ln=True, align='C')
pdf.ln(10)

# Tartalom hozzáadása
pdf.set_font("Arial", size=12)
content = """\
1. 🌍 Exteroceptív = Külvilágból származó ingerek érzékelése
Receptorok helye: bőr, szem, fül, orr, nyelv
Érzékelt dolgok: fény, hang, szag, íz, tapintás, hő, fájdalom
Példák: látsz valamit, megérintesz egy tárgyat, hallasz egy hangot

2. 🏃‍♂️ Proprioceptív = A test helyzetének, mozgásának érzékelése
Receptorok helye: izmok, ízületek, inak
Érzékelt dolgok: testtartás, mozgás, izomfeszülés
Példák: tudod, hol van a karod akkor is, ha nem nézed; egyensúlyozás

3. 🫀 Interoceptív = A belső szervek állapotának érzékelése
Receptorok helye: belső szervek (gyomor, tüdő, szív stb.)
Érzékelt dolgok: éhség, teltség, szívverés, légzés, fájdalom belül
Példák: érzed, hogy korog a gyomrod, szomjas vagy, szívdobogás

Mini összefoglaló mondat:
Exteroceptív – kívülről
Proprioceptív – testhelyzet
Interoceptív – belülről
"""

pdf.multi_cell(0, 10, txt=content)

# PDF mentése
pdf.output("Erzekeles_tipusai_tanulokartya.pdf")
