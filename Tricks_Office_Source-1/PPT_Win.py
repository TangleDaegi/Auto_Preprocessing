import win32com.client

def AutoFont2(file,Tpath,Rpath,FName):
    powerpoint = win32com.client.Dispatch('PowerPoint.Application')
    Sepa = '\\'
    Tpath = Tpath.replace("/","\\")
    Rpath = Rpath.replace("/","\\")
    ppt = powerpoint.Presentations.Open (Tpath + Sepa + file, WithWindow=False)

    for slide in ppt.Slides:
        for shape in slide.shapes:
            if shape.HasTextFrame == -1:
                shape.TextFrame.TextRange.Font.NameFarEast = FName
                shape.TextFrame.TextRange.Font.Name = FName
            if shape.HasTable == -1:
                for row in shape.Table.Rows:
                    for cell in row.cells:
                        cell.Shape.TextFrame.TextRange.Font.NameFarEast = FName
                        cell.Shape.TextFrame.TextRange.Font.Name = FName
            try:
                for GI in shape.GroupItems:
                    GI.TextFrame.TextRange.Font.NameFarEast = FName
                    GI.TextFrame.TextRange.Font.Name = FName
            except:
                pass

    ppt.SaveAs (Rpath + Sepa + file)
    ppt.Close ()

Tpath = 'D:/Python/TricksOffice/Sample'
Rpath = 'D:/Python/TricksOffice/Result'
Fname = '맑은 고딕'
file = 'Sample.pptx'

AutoFont2(file,Tpath,Rpath,Fname)

