import os

input_directory = r'D:\SGH\hw'
output_directory = r'D:\SGH\HW2'
def process_and_write_csv(input_filename):
    input_file_path = os.path.join(input_directory, input_filename)
    output_filename = f'{os.path.splitext(input_filename)[0]}_with_percentage_change.csv'
    output_file_path = os.path.join(output_directory, output_filename)

    print(f'Trying to read {os.path.abspath(input_file_path)}')

    m = []

    with open(input_file_path, 'r') as f:
        header = f.readline().strip()
        print(f'Header: {header}')

        for line in f:
            data = line.strip().split(',')
            date, open_price, high, low, close, adj_close, volume = data
            percentage_change = (float(close) - float(open_price)) / float(open_price) * 100
            data.append(f'{percentage_change:.2f}')

            m.append(data)

    with open(output_file_path, 'w') as new_file:
        new_file.write(f'{header},Percentage Change\n')

        for row in m:
            new_file.write(','.join(row) + '\n')

    print(f'File with percentage change for {input_filename} saved at: {os.path.abspath(output_file_path)}')

process_and_write_csv('GOOG.csv')
process_and_write_csv('IBM.csv')
process_and_write_csv('MSFT.csv')
