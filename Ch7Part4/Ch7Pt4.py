# Week 12, ICA 2
import matplotlib.pyplot as plt

def main():
    premier = ('Liverpool', 'Chelsea', 'Arsenal', 'Southampton')
    mls = ('LAFC', 'LA Galaxy', 'DC United', 'Sporting KC')
    for epl in premier:
        print(epl)
    print()
    for x in range(len(mls)):
        print(mls[x])
    # unpack mls tuple
    mls1, mls2, mls3, mls4 = mls
    print(mls1, 'and', mls2, 'and', mls3, 'and', mls4)
    soccer_teams = list(premier)
    soccer_teams.append(mls1)
    soccer_teams.append(mls2)
    soccer_teams.append(mls3)
    soccer_teams.append(mls4)
    print()
    print(soccer_teams)
    soccer_teams2 = tuple(soccer_teams)
    print(soccer_teams2)
    
    # Part 2
    plt.figure()
    # Create lists with the X,Y coordinates of each data point.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Build the line graph.
    plt.plot(x_coords, y_coords, marker='o')

    # Add a title.
    plt.title('Sales by Year')

    # Add labels to the axes.
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # Customize the tick marks.
    plt.xticks([0, 1, 2, 3, 4],['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5],['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    
    # Add a grid.
    plt.grid(True)

    # Display the line graph.
    # plt.show()

    # Part 3
    plt.figure()
    # Create a list with the X coordinates of each bar's left edge.
    left_edges = [0, 10, 20, 30, 40]

    # Create a list with the heights of each bar.
    heights = [100, 200, 300, 400, 500]

    # Create a variable for the bar width.
    bar_width = 10

    # Build the bar chart.
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'y', 'k'))

    # Add a title.
    plt.title('Sales by Year')

    # Add labels to the axes.
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # Customize the tick marks.
    plt.xticks([5, 15, 25, 35, 45],['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # Display the bar chart.
    # plt.show()

    # Part 4
    plt.figure()
    # Create a list of sales amounts.
    sales = [100, 400, 300, 600]
    
    # Create a list of labels for the slices.
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']

    # Create a pie chart from the values.
    plt.pie(sales, labels=slice_labels, colors=('r','g','m','b'))

    # Add a title.
    plt.title('Sales by Quarter')

    # Display the pie chart.
    plt.show()

main()