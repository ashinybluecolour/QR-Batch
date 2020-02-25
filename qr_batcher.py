#! /usr/bin/env python3

import qrcode
import os
from PIL import Image
from fpdf import FPDF

def help():
 print("Usage: "+os.sys.argv[0])
 print("      --prefix <prefix>")
 print("      --start <start#>")
 print("      --increment <increment by #>")
 print("      --end <terminate at #>")

if (len(os.sys.argv) < 9):
 help()
 os.sys.exit(0)
for i in range(0, len(os.sys.argv)):
 arg = os.sys.argv[i]
 if (arg == "--prefix"):
  prefix = os.sys.argv[i+1]
 elif (arg == "--start"):
  start = os.sys.argv[i+1]
 elif (arg == "--increment"):
  increment = os.sys.argv[i+1]
 elif (arg == "--end"):
  end = os.sys.argv[i+1]
 else:
  if ("--" in arg):
   print ("unknown option: \""+arg+"\"")
   help()
   os.sys.exit(0)

qr = qrcode.QRCode(
 version = 1,
 error_correction=qrcode.constants.ERROR_CORRECT_H,
 box_size = 1,
 border = 0
)

try:
 os.makedirs("QR_Png")
 os.makedirs("QR_Pdf")
except:
 pass

pdf = FPDF('P', 'in', 'A4')
i = int(start)
x = 0

while i <= int(end):
 if (x%48 == 0):
  x = 0
  pdf.add_page()
   
 file_name = prefix+str(i)
 qr.add_data(prefix+str(i))
 qr.make(fit=True)
 img = qr.make_image(fill_color="black", back_color="white")
 img.save("QR_Png/"+file_name+".png")
 qr.clear()
 pdf.image("QR_Png/"+file_name+".png", 1.2*(x%6)+0.635, 1.2*(x//6)+1, 1, 1)
 #img = Image.open("QR_Png/"+file_name+".png")
 #img.save("QR_Pdf/"+file_name+".pdf", "PDF", Quality = 100)
 i += int(increment)
 x += 1
pdf.output(prefix+".pdf", "F")
pdf.close()

