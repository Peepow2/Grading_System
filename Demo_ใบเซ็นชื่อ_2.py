import fpdf
import os
import time
import ID

ss = time.time()
pdf = fpdf.FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(True, margin = 15)
pdf.set_top_margin(15)
pdf.set_left_margin(15)
pdf.set_right_margin(15)
pdf.add_font('Th_sarabun_psk', '', 'THSarabun.ttf')
pdf.add_font('Th_sarabun_psk', 'B', 'THSarabun Bold.ttf')

ID.reset_pass()
HEADER = ["ลำดับ", "เลขที่นั่งสอบ", "รหัสประจำตัวสอบ", "ชื่อ - นามสกุล", "ลายมือชื่อ"]
DATA =  ["นายแมนยู ดูแล้วแพ้", "นายลิเวอร์พูล แพ้บ๊วยคูล ๆ",
         "นายเซลซี มีแต่เงิน", "นายอาร์เซนอล ราย่าบอลหลุด",
         "นายสเปอร์ส ละเมอหาเคน", "นายแมนซิ ขาดเป๊บซิ",
         "นายมาดริด พิชิตสี่แชมป์", "นายบาร์ซ่า มาแล้วคับ",
         ]
size = (10, 25, 30, 65, 40)

NO_Room = 'x 401 402 404 405 501 502 504 505 601 602'.split()
R = 1
seq = 0
B = 35
N = 321
Page = 0
while R <= N:
    if R % 35 == 1:
        seq = 1
        Page += 1
        
        pdf.add_page()
        pdf.set_font('Th_sarabun_psk', 'B', 14)
        pdf.cell(180, 7, 'ใบเซ็นชื่อผู้เข้าสอบ', border = 0, align = 'C')
        pdf.ln()
        pdf.cell(180, 7, 'โครงการจำลองการสอบเข้าศึกษาต่อคณะวิศวกรรมศาสตร์ โดยชมรม FECamp CU ปีการศึกษา 2566', border = 0, align = 'C')
        pdf.set_line_width(0.5)
        pdf.line(15, 30, 195, 30)

        pdf.set_font('Th_sarabun_psk', '', 14)
        pdf.ln(10)
        pdf.cell(135, 7, 'วิชา: Pretest FECamp17', border = 0, align = 'L')
        pdf.ln()
        pdf.cell(120, 7, 'วันที่สอบ: วัน______ที่ XX พฤษภาคม 2567', border = 0, align = 'L')
        pdf.cell(50, 7, 'เวลาสอบ: 8:30 – 11:30 น', border = 0, align = 'L')
        pdf.ln()
        pdf.cell(120, 7, 'สนามสอบ: จุฬาลงกรณ์มหาวิทยาลัย', border = 0, align = 'L')
        pdf.cell(50, 7, f'ห้องสอบที่: {Page} ({NO_Room[Page]})', border = 0, align = 'L')
        pdf.ln(10)

        pdf.set_line_width(0.2)
        with pdf.table(width = 180, line_height = 6, col_widths = size, \
                        text_align = ("CENTER")) as table:
            headings = table.row()
            for d in HEADER:
                headings.cell(d)

    with pdf.table(width = 180, line_height = 6, first_row_as_headings = False, col_widths = size, \
                   text_align=("CENTER", "CENTER", "CENTER", "LEFT", "CENTER")) as table:
        while True:
            row = table.row()
            ROW = [str(R), str(((R-1) % B) + 1), ID.get_ID(), DATA[(R-1) % 8], '']
            for datum in ROW:
                row.cell(datum)
            R += 1
            seq += 1
            if seq >= B: break

pdf.output("Simple.pdf") # Create ใบรายชื่อ
# ----------------------------------------------- # 
PRINT = False # ปริ้นไฟล์
if PRINT: os.startfile("Simple.pdf", "print")
# ----------------------------------------------- # 
print("Finished")
total = time.time() - ss
print('TIME USED =', int(total // 3600), 'hour', int(total // 60), 'min', int(total % 60) + 1, 'seconds')
#os.remove("Simple.pdf")
