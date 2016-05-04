# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag1_40223153a = Blueprint('ag1_40223153a', __name__, url_prefix='/ag1_40223153a', template_folder='templates')

@ag1_40223153a.route('/aaaa')
def aaaa():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic6 = cmbr.dup()
    basic6.rotate(150)
    basic6.translate(0, 40)
    
    basic7 = cmbr.dup()
    basic7.rotate(210)
    basic7.translate(40, 40)
    
    basic8 = cmbr.dup()
    basic8.rotate(270)
    basic8.translate(30, 57.5)
    
    basic9 = cmbr.dup()
    basic9.rotate(270)
    basic9.translate(20, 0)
    
    basic10 = cmbr.dup()
    basic10.rotate(270)
    basic10.translate(40, 0)
    
    basic11 = cmbr.dup()
    basic11.rotate(180)
    basic11.translate(40, 0)
    
    basic12 = cmbr.dup()
    basic12.rotate(180)
    basic12.translate(40, 20)
    
    basic13 = cmbr.dup()
    basic13.rotate(180)
    basic13.translate(0, 20)
   
    basic14 = cmbr.dup()
    basic14.rotate(180)
    basic14.translate(0, 0)
    
    basic15 = cmbr.dup()
    basic15.rotate(360)
    basic15.translate(40, 0)
    
    basic16 = cmbr.dup()
    basic16.rotate(150)
    basic16.translate(70, 40)
    
    basic17 = cmbr.dup()
    basic17.rotate(210)
    basic17.translate(110, 40)
    
    basic18 = cmbr.dup()
    basic18.rotate(270)
    basic18.translate(100, 57.5)

    basic19 = cmbr.dup()
    basic19.rotate(270)
    basic19.translate(90, 0)
   
    basic20 = cmbr.dup()
    basic20.rotate(270)
    basic20.translate(110, 0)
    
    basic21 = cmbr.dup()
    basic21.rotate(180)
    basic21.translate(110, 0)
    
    basic22 = cmbr.dup()
    basic22.rotate(180)
    basic22.translate(110, 20)
    
    basic23 = cmbr.dup()
    basic23.rotate(180)
    basic23.translate(70, 20)
    
    basic24 = cmbr.dup()
    basic24.rotate(180)
    basic24.translate(70, 0)
    
    basic25 = cmbr.dup()
    basic25.rotate(360)
    basic25.translate(110, 0)
    
    basic26 = cmbr.dup()
    basic26.rotate(150)
    basic26.translate(140, 40)
    
    basic27 = cmbr.dup()
    basic27.rotate(210)
    basic27.translate(180, 40)
    
    basic28 = cmbr.dup()
    basic28.rotate(270)
    basic28.translate(170, 57.5)
    
    basic29 = cmbr.dup()
    basic29.rotate(270)
    basic29.translate(160, 0)
    
    basic30 = cmbr.dup()
    basic30.rotate(270)
    basic30.translate(180, 0)
    
    basic31 = cmbr.dup()
    basic31.rotate(180)
    basic31.translate(180, 0)
    
    basic32 = cmbr.dup()
    basic32.rotate(180)
    basic32.translate(180, 20)
    
    basic33 = cmbr.dup()
    basic33.rotate(180)
    basic33.translate(140, 20)
    
    basic34 = cmbr.dup()
    basic34.rotate(180)
    basic34.translate(140, 0)
    
    basic35 = cmbr.dup()
    basic35.rotate(360)
    basic35.translate(180, 0)
    
    basic36 = cmbr.dup()
    basic36.rotate(150)
    basic36.translate(210, 40)
    
    basic37 = cmbr.dup()
    basic37.rotate(210)
    basic37.translate(250, 40)
    
    basic38 = cmbr.dup()
    basic38.rotate(270)
    basic38.translate(240, 57.5)
    
    basic39 = cmbr.dup()
    basic39.rotate(270)
    basic39.translate(230, 0)
    
    basic40 = cmbr.dup()
    basic40.rotate(270)
    basic40.translate(250, 0)
    
    basic41 = cmbr.dup()
    basic41.rotate(180)
    basic41.translate(250, 0)
    
    basic42 = cmbr.dup()
    basic42.rotate(180)
    basic42.translate(250, 20)
    
    basic43 = cmbr.dup()
    basic43.rotate(180)
    basic43.translate(210, 20)
    
    basic44 = cmbr.dup()
    basic44.rotate(180)
    basic44.translate(210, 0)
    
    basic45 = cmbr.dup()
    basic45.rotate(360)
    basic45.translate(250, 0)
     
    basic46 = cmbr.dup()
    basic46.rotate(360)
    basic46.translate(70, 0)
    
    basic47 = cmbr.dup()
    basic47.rotate(360)
    basic47.translate(140, 0)
    
    basic48 = cmbr.dup()
    basic48.rotate(360)
    basic48.translate(210, 0)
    
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic38)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)
    cmbr.appendPath(basic43)
    cmbr.appendPath(basic44)
    cmbr.appendPath(basic45)
    cmbr.appendPath(basic46)
    cmbr.appendPath(basic47)
    cmbr.appendPath(basic48)
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 0.9, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 0.9, rot)

O(0, 0, 0, 0, 0, "green", True, 4)
</script>

<script type="text/python" src="/ag1_40323105/task1"></script>

</body>
</html>
'''
    return outstring