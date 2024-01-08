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


HEADER = ["ลำดับ", "เลขที่นั่งสอบ", "รหัสประจำตัวสอบ", "ชื่อ - นามสกุล", "ลายมือชื่อ"]
DATA =  ["แมนยู ดูแล้วท้อ", "แมนยู ฮาโอนาน่า",
         "ลิเวอร์พูล กรูไม่ชอบ", "ลิเวอร์พูล กรูหมั่นไส้",
         "เซลซี มีแต่เงิน", "อาร์เซนอล ราย่าบอลหลุด",
         "สเปอร์ส ละเมอหาเคน", "แมนซิ ขาดเป๊บซิ",
         "มาดริด พิชิตสี่แชมป์", "บาร์ซ่า มาแล้วคับ",
         ]
DATA.sort()
DATA *= 30
size = (10, 25, 30, 65, 40)
NO_Room = 'x 202 203 204 205 206 207 208 302 303 304 305 306 309 315'.split()
cum_num_na = 'นาย นางสาว'.split()
B = 35
Page = 0
stu_ID = '00000000'
for R in range(len(DATA)):
    if R % B == 0:
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
        pdf.cell(120, 7, 'สนามสอบ: ตึก 3 คณะวิศวกรรมศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย', border = 0, align = 'L')
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
        stu_ID = ID.get_ID(stu_ID)
        C = cum_num_na[ID.Rint(0, 1)]
        ROW = [str(R + 1), str((R % B) + 1), stu_ID, C + DATA[R], '']
        row = table.row()
        for datum in ROW:
            row.cell(datum)

pdf.output("Simple.pdf") # Create ใบรายชื่อ
# ----------------------------------------------- # 
PRINT = False # ปริ้นไฟล์
if PRINT: os.startfile("Simple.pdf", "print")
# ----------------------------------------------- # 
print("Finished")
total = time.time() - ss
print(total)
print('TIME USED =', int(total // 3600), 'hour', int(total // 60), 'min', int(total % 60) + 1, 'seconds')
#os.remove("Simple.pdf")
