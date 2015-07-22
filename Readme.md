Coffee Meets Bagel dating website match exporter.  Provides an csv file dump of of user data along with image links.  Uses selenium to scrap web, vb script to size and laod images, and pandas/matlablib to provide analysis.  

Code Snippet for VB image:

Dim url_column As Range
Dim image_column As Range

Set url_column = Worksheets(1).UsedRange.Columns("A")
Set image_column = Worksheets(1).UsedRange.Columns("B")

Dim i As Long
For i = 1 To url_column.Cells.Count

  With image_column.Worksheet.Pictures.Insert(url_column.Cells(i).Value)
    .Left = image_column.Cells(i).Left
    .Top = image_column.Cells(i).Top
    image_column.Cells(i).EntireRow.RowHeight = .Height
  End With

Next