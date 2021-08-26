import gspread_formatting as gsfm

class bg_styles:
    red = gsfm.CellFormat(backgroundColor=gsfm.Color(red=1.0))
    green = gsfm.CellFormat(backgroundColor=gsfm.Color(green=1.0))
    black = gsfm.CellFormat(backgroundColor=gsfm.Color(red=0.0, green=0.0, blue=0.0, alpha=1.0))

