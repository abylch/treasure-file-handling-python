משחק מציאת המטמון
כתוב תוכנית פייטון למשחק מציאת המטמון .שלב ראשון - יצר קובץ חדש (או מחק את הקובץ בעת איתחולו) 
ובתוכו רצף הספרות מ - 0 ועד 9 .כל ספרה תופיע מספר אקראי של פעמים [20-1 [פעמים. אחרי ספרת ה - 9 
האחרונה כתוב את המילה . TREASUREלאחר מכן , שוב כתוב את הספרות בסדר יורד כלומר, מ9- ועד 0 .כל 
ספרה תופיע מספר אקראי של פעמים [20-1 [פעמים .לדוגמא
- 0000000000000111111111111222222222222223333333333333333444444444 
5555555555555555555555555555555555555555556666666666666666666777 
8888888888888999999999999999999999999999999 TREASURE 999999999999 
9999999999999999999999998888888888888888888888887777777777777777 
6666666666666666666666666666655555555555555555555555555444444444 
4444444333333333333333333332222222222222222222221111111111111111
שלב שני - פתח את הקובץ לקריאה בלבד ותן למשתמש לזוז קדימה או אחורה כרצונו. המשתמש בעצם יזיז 
את הסמן עד אשר יפגע באחד מאותיות ה . TREASURE -בכל פעם הדפס למשתמש את התו "שנחת" עליו .
אחרי שמצא את האוצר הדפס כמה תורים זה לקח לדוגמא
Where you want to move? [1- forward 2-backwards] 
1 
How many characters? 
30 You hit “1” 
… again … until hit one of the “TREASURE” letters…
אתגר: נהל טבלה של 10 התוצאות הטובות ביותר (בקובץ). בסוף כל משחק- בדוק אם השחקן הצליח לפגוע 
במספר ניחושים הנמוך מהדירוג ה - 10 בטבלה. אם כן, קלוט את שמו והכנס את תוצאתו לקובץ במקום 
המתאים (כל שורה בקובץ תכיל תוצאה ושם של שחקן( . )כמובן שבפעם הראשונה מכיוון שהקובץ יהיה ריק, 
כל תוצאה תוכנס לקובץ וכו)



Python allows users to handle files (read, write, save and delete files and many more).

ex:

# Open function to open the file "myfile.txt"   
# (same directory) in read mode and store 
# it's reference in the variable file1 
    
file1 = open("myfile.txt") 
    
# Reading from file 
print(file1.read()) 
    
file1.close() 

#
with open('read.txt', 'w') as file:
      
    books = ['Welcome\n', 
             'Geeks\n', 
             'to\n', 
             'Geeks\n',
             'for\n', 
             'Geeks\n', 
             'world\n']
      
    file.writelines("% s\n" % data for data in books)



Following are the most commonly used access modes:

Read Only (‘r’): Open text file for reading.
Write Only (‘w’): Open the file for writing.
Append Only (‘a’): Open the file for writing. The data being written will be inserted at the end, after the existing data.
Read and Write (‘r+’): Open the file for reading and writing.