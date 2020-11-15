import statzcw as st
import csv


data_files = ['dataZero.csv', 'dataOne.csv', 'dataTwo.csv', 'dataThree.csv']
for file in data_files:
    print("File name:", file)

    x = []
    y = []

    with open(file) as f:
        f.readline()  # Skip header line
        csvin = csv.reader(f)
        for row in csvin:
            x.append(float(row[0]))
            y.append(float(row[1]))

    print("Count of X:", st.zcount(x))
    print("Count of Y:", st.zcount(y))
    print("Mean of X:", st.zmean(x))
    print("Mean of Y:", st.zmean(y))
    print("Mode of X:", st.zmode(x))
    print("Mode of Y:", st.zmode(y))
    print("Median of X:", st.zmedian(x))
    print("Median of Y:", st.zmedian(y))
    print("Standard Deviation of X:", st.zstddev(x))
    print("Standard Deviation of Y:", st.zstddev(y))
    print("Standard Error of X:", st.zstderr(x))
    print("Standard Error of Y:", st.zstderr(y))
    print("Variance of X:", st.zvariance(x))
    print("Variance of Y:", st.zvariance(y))
    print("Correlation of X and Y:", st.zcorr(x,y))

    print()
