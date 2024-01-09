import fpdf
import os
import time

ss = time.time()
pdf = fpdf.FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(True, margin = 15)
pdf.set_top_margin(15)
pdf.set_left_margin(15)
pdf.set_right_margin(15)
pdf.add_font('Th_sarabun_psk', '', 'THSarabun.ttf')
pdf.add_font('Th_sarabun_psk', 'B', 'THSarabun Bold.ttf')
pdf.add_page()

pdf.set_font('Th_sarabun_psk', 'B', 14)
pdf.cell(180, 7, 'ใบเซ็นชื่อผู้เข้าสอบ', border = 0, align = 'C')
pdf.ln()
pdf.cell(180, 7, 'โครงการจำลองการสอบเข้าศึกษาต่อคณะวิศวกรรมศาสตร์ โดยชมรม FECamp CU ปีการศึกษา 2566', border = 0, align = 'C')
pdf.set_line_width(0.5)
pdf.line(15, 30, 195, 30)

pdf.set_font('Th_sarabun_psk', '', 14)
pdf.ln(10)
pdf.cell(135, 6, 'วิชา: Pretest FECamp17', border = 0, align = 'L')
pdf.ln()
pdf.cell(120, 6, 'วันที่สอบ: วัน______ที่ XX พฤษภาคม 2567', border = 0, align = 'L')
pdf.cell(50, 6, 'เวลาสอบ: 8:30 – 11:30 น', border = 0, align = 'L')
pdf.ln()
pdf.cell(120, 6, 'สนามสอบ: จุฬาลงกรณ์มหาวิทยาลัย', border = 0, align = 'L')
pdf.cell(50, 6, 'ห้องสอบที่: 1 (XXX)', border = 0, align = 'L')
pdf.ln(8)

pdf.set_line_width(0.2)
HEADER = ["ลำดับ", "เลขที่นั่งสอบ", "รหัสประจำตัวสอบ", "ชื่อ - นามสกุล", "ลายมือชื่อ"]
DATA =  [["68000001", "นายแมนยู ดูแล้วแพ้"],
         ["68000002", "นายลิเวอร์พูล แพ้บ๊วยคูล ๆ"],
         ["68000003", "นายเซลซี มีแต่เงิน"],
         ["68000004", "นายอาร์เซนอล ราย่าบอลหลุด"],
         ["68000005", "นายสเปอร์ส ละเมอหาเคน"],
         ["68000006", "นายแมนซิ ขาดเป๊บซิ"],
         ["68000007", "นายมาดริด พิชิตสี่แชมป์"],
         ["68000008", "นายบาร์ซ่า มาแล้วคับ"],
         ]

pdf.set_font('Th_sarabun_psk', '', 14)
size = (10, 25, 30, 65, 40)
with pdf.table(width = 180, line_height = 6, col_widths = size, \
               text_align = ("CENTER")) as table:
    headings = table.row()
    for d in HEADER:
        headings.cell(d)

with pdf.table(width = 180, line_height = 6, first_row_as_headings = False, col_widths = size, \
               text_align=("CENTER", "CENTER", "CENTER", "LEFT", "CENTER")) as table:
    cnt = 1
    while True:
        for data_row in DATA:
            row = table.row()
            for datum in ([str(cnt), str(cnt)] + data_row + ['']):
                row.cell(datum)
            cnt += 1
            if cnt > 30: break
        if cnt > 30: break

pdf.output("Simple.pdf") # Create ใบรายชื่อ
# ----------------------------------------------- # 
PRINT = True # ปริ้นไฟล์
if PRINT: os.startfile("Simple.pdf", "print")
# ----------------------------------------------- # 
print("Finished")
total = time.time() - ss
print('TIME USED =', int(total // 3600), 'hour', int(total // 60), 'min', int(total % 60) + 1, 'seconds')
#os.remove("Simple.pdf")
