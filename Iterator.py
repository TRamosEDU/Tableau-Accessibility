from tableaudocumentapi import Workbook

# Replace with the path to your Tableau workbook
workbook_path = 'C:\\Users\\Yago\\Desktop\\Work Stuff\\Acessability Tableau\\Customer Dashboard Test HCM 3.twbx'

# Open the workbook
workbook = Workbook(workbook_path)

# Iterate through each dashboard in the workbook
for dashboard in workbook.dashboards:
    print(f'Dashboard: {dashboard.name}')

    # Iterate through each worksheet in the dashboard
    for worksheet in dashboard.worksheets:
        # Get the position and size of the worksheet
        x = worksheet.x
        y = worksheet.y
        width = worksheet.width
        height = worksheet.height

        print(f'Worksheet: {worksheet.name}, X: {x}, Y: {y}, Width: {width}, Height: {height}')