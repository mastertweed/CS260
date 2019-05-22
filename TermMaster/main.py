from selenium import webdriver
import time
from classList import schools
import xlsxwriter

workbook = xlsxwriter.Workbook('Course_List.xlsx')
worksheet = workbook.add_worksheet()

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

row = 1


def pull(start):
    a = []
    for ii in driver.find_elements_by_class_name("odd"):
        a.append(ii.text[start:])

    for ii in driver.find_elements_by_class_name("even"):
        a.append(ii.text[start:])

    return a


driver = webdriver.Chrome(executable_path="/Users/alexTweed/PycharmProjects/TermMaster/drivers/chromedriver")

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://termmasterschedule.drexel.edu/webtms_du/app")

driver.find_element_by_link_text("Winter Quarter 18-19").click()


# Iterate through all the schools, subjects and courses

for school in schools:
    try:
        driver.find_element_by_link_text(school).click()
        time.sleep(0.25)
    except:
        print('Error: No School')

    subjectList = pull(2)

    subjectCount = 0
    for subject in subjectList:
        # FOR TESTING
        if subjectCount < 2:
            subjectCount += 1
            driver.find_element_by_link_text(subject).click()

            # 1 = Subject Code
            # 2 = Course No.
            # 3 = Instr Type
            # 4 = Instr Method
            # 5 = Sec
            # 6 = CRN
            # 7 = Course Title
            # 8 = Days  /  Time
            # 9 = Instructor

            courseList = pull(0)
            print(int(((len(courseList)-1)/2)))

            for course in range(2,int(((len(courseList)-1)/2)+2)):

                xp = '/html/body/table/tbody/tr[2]/td/table/tbody/tr[6]/td/table/tbody/tr'
                xp = xp + '[' + str(course) + ']/td[6]'

                # print(driver.find_element_by_xpath(xp).text)
                driver.find_element_by_xpath(xp).click()

                # 0 = CRN
                # 1 = Subject Code
                # 2 = Course Number
                # 3 = Section
                # 4 = Credits
                # 5 = Title
                # 6 = Campus
                # 7 = Instructor(s)
                # 8 = Instruction Type
                # 9 = Instruction Method
                # 10 = Max Enroll
                # 11 = Enroll

                temp = []

                # Iterate through all the course information table
                for i in [0, 2, 5, 11]:
                # for i in range(12):
                    num = i+1
                    xp2 = '/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr'
                    xp2 = xp2 + '[' + str(num) + ']/td[2]'
                    temp.append(str(row))
                    temp.append(driver.find_element_by_xpath(xp2).text)

                print(temp)

                time.sleep(0.1)
                #
                # for col in range(len(temp)):
                #     cell = alpha[col] + str(row)
                #     worksheet.write(cell, temp[col])
                #
                # row += 1

                # Return to course list
                driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/ul/li[4]').click()


            # Return to colleges/subjects
            driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/ul/li[3]').click()

            # workbook.close()

time.sleep(0.5)

driver.close()
driver.quit()
print("\nTest Completed")