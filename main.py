from bs4 import BeautifulSoup
import requests
import itertools

coursesWanted = input("How many courses do you want?\n")
courseNames = []
courseInfo = []

print("Enter the course code followed by the enter key for each course:\n")
for _ in range(int(coursesWanted)):
    courseCode = input()
    courseNames.append(courseCode)

def InfoToArray(section):  # type: ignore
    sectionInfo = []
    for i in range(len(section)):
        sectionInfo.append(section[i].text.replace('\n', '').replace('\t', '').strip())
        
    return sectionInfo

for i in range(len(courseNames)):
    html_text = requests.get('https://www.sfu.ca/students/calendar/2023/spring/courses/'+courseNames[i][:4]+'/'+courseNames[i][-3:]+'.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    sectionRows = soup.find_all('tr', class_ = 'main-section')
    sections = []
    for i in range(len(sectionRows)):
        row = sectionRows[i].find_all('td')  # type: ignore
        sections.append(InfoToArray(row))
    courseInfo.append(sections)

#print(courseInfo)

masterSchedule = list(itertools.product(*courseInfo))

# for i in range(len(masterSchedule)):
#     print(masterSchedule[i])
#     print()

def changeFormat(arr):
    for i in range(len(arr)):
        j = 0
        while(j < len(arr[i])-1):
            if (arr[i][j]+arr[i][j+1] == 'PM'):
                
                




def hasConflict(arr):
    changeFormat(arr)

timeIndex = 2
for i in range(len(masterSchedule)):
    timeArray = []
    for j in range(len(masterSchedule[i])):
        timeArray.append(masterSchedule[i][j][timeIndex])
    print(timeArray)
    print()
    #if conflict then do not add to schedule
    hasConflict(timeArray)
    #else add thing


    






