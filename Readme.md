Coffee Meets Bagel dating website match exporter.  Provides an csv file dump of of user data along with image links.  Uses selenium to scrap web, vb script to size and load images, and pandas/matlablib to provide analysis.  

## Sample 

![alt text](https://raw.githubusercontent.com/eugenechung81/cmb-excel-export/master/report/sample.png "Image")

## Analysis

Age

![alt text](https://raw.githubusercontent.com/eugenechung81/cmb-excel-export/master/report/age.png "Image")

> mean     28.313131  
> std       1.475283  
> min      24.000000  
> 25%      27.000000  
> 50%      29.000000  
> 75%      29.500000  
> max      30.000000  

Histogram of Age Distribution (mu = 28.31, sigma = 1.47)

![alt text](https://raw.githubusercontent.com/eugenechung81/cmb-excel-export/master/report/age-hist.png "Image")

Appears CMB algo tailors matches to users' age.  Also indicates higher percentage of older users in the CMB pool. 

Nationality 

![alt text](https://raw.githubusercontent.com/eugenechung81/cmb-excel-export/master/report/nationality.png "Image")

Nationality
> N/A                        1  
> American                   2  
> Canadian                   1  
> Chinese                    5  
> Chinese/Taiwanese          1  
> Chinse                     1  
> Korean                    21  
> Korean American            7  
> Korean-American            4  
> Taiwanese                  4  
> Taiwanese-American         1  
> USA                        2  
> Vietnamese and Chinese     1  

Koreans are dominating CMB in the asian ethnicity group. 

Religion 

![alt text](https://raw.githubusercontent.com/eugenechung81/cmb-excel-export/master/report/religion.png "Image")

Same with Christians. 

Height

![alt text](https://raw.githubusercontent.com/eugenechung81/cmb-excel-export/master/report/height.png "Image")

> mean     63.69697  
> std       1.69305  
> min      60.00000  
> 25%      62.00000  
> 50%      64.00000  
> 75%      65.00000  
> max      68.00000  

Average height is: 5'3 

## Code Snippet for VB image:

'''
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
'''
