import pandas as pd
import sys

NAME_COL = "Name"

# Change these according to the registration form
DETAIL_COL_IDS = ["Ruoka / Meal", "Viini / Wine", "Snapsi / Scnapps", "Avec", "Sima / Mead"]

# These are how the above categories are displayed on the cards
# Customize these to your liking
DETAIL_COL_SHOW = ["Meal", "Wine", "Scnapps", "Avec", "Sima"]

CARDS_PER_ROW = 3
CARDS_PER_COL = 5

data = pd.read_csv(sys.argv[1])
filename = sys.argv[2]

# Kinda hardcoded
# Helper function to parse the english part of a value, modify when needed
def parseval(val):
    if "/" in str(val):
        return str(val).split("/")[1].strip()
    return val


def ashtmltable(vals):
    rowstr = "<div><table cellspacing=0><tbody>\n"
    rowstr += "<tr><td colspan=2 class=center>"
    rowstr += str(vals[NAME_COL])
    rowstr += "</td></tr>"
    for i in range(len(DETAIL_COL_IDS)):
        rowstr += "<tr><td>"
        rowstr += str(DETAIL_COL_SHOW[i])
        rowstr += "</td><td>"
        rowstr += str(parseval(vals[DETAIL_COL_IDS[i]]))
        rowstr += "</td></tr>\n"
    rowstr += "</tbody></table></div>"
    return rowstr

def savehtml(htmlstring, name):
    with open(name + ".html", "w") as file:
        file.write(htmlstring)

# Add fonts here
tblsstr = """<html><head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet"> """

# Customize style here
tblsstr += """<style>div{width:300px;height:200px;border:1px solid grey;display:flex;align-items:center; padding:5px;}
                .center{text-align:center;}
                body{display:grid;grid-template-columns:1fr 1fr 1fr;width:900px; font-family: 'Libre Baskerville', serif;}
                tr:not(:first-child) td:first-child{white-space:nowrap; font-size:0.7rem;} 
                tr:first-child td{font-size:1.2rem; font-weight:bold; padding-bottom:10px} 
                table{width:300px;}
                *{box-sizing:border-box}
                </style></head>"""
tblsstr += "<body>"

# Reverse names used for tistiS :D
# tr:first-child td{font-size:1.2rem; font-weight:bold; padding-bottom:10px; transform: scaleX(-1)}

for i, row in data.iterrows():
    vals = {NAME_COL: row[NAME_COL]}
    for id in DETAIL_COL_IDS:
        vals[id] = row[id]
    tblsstr += ashtmltable(vals)
tblsstr += "</body></html>"
        
savehtml(tblsstr, filename)