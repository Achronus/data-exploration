# Retail Customer Analysis

Having worked at Tesco, I've always wanted to learn more about customers buying habits. Unfortunately, I didn't have access to any of their analytics data. So instead, I found one that could be related based on what I know about the company.

The dataset used was found on the UC Irvine ML archive and is an [online retail store dataset](https://archive.ics.uci.edu/dataset/502/online+retail+ii).

Here's what we know initially know about the data:

- It has two sheets, one for 2009-2010 and 2010-2011.
- 7 variables (columns) per record (row).

Variable information:

- `InvoiceNo`: Invoice number. Nominal. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter 'c', it indicates a cancellation.
- `StockCode`: Product (item) code. Nominal. A 5-digit integral number uniquely assigned to each distinct product.
- `Description`: Product (item) name. Nominal.
- `Quantity`: The quantities of each product (item) per transaction. Numeric.
`InvoiceDate`: Invice date and time. Numeric. The day and time when a transaction was generated.
- `UnitPrice`: Unit price. Numeric. Product price per unit in sterling (£).
`CustomerID`: Customer number. Nominal. A 5-digit integral number uniquely assigned to each customer.
- `Country`: Country name. Nominal. The name of the country where a customer resides.

Our goal is to identify customer patterns using clustering techniques. For simplicity, we'll focus on the first sheet (2009-2010) which has 525,461 records.

## Thoughts on the Project

Exploring this dataset was a lot of fun. It's messy and provides a variety of random records that shouldn't be there based on initial expectations.

For example, the `StockCode` column should only contain 5-digit numeric codes. Yet, we get this mess too!

`['POST', 'D', 'DCGS0058', 'DCGS0068', 'DOT', 'M', 'DCGS0004', 'DCGS0076', 'C2', 'BANK CHARGES', 'DCGS0003', 'TEST001', 'gift_0001_80', 'DCGS0072', 'gift_0001_20', 'DCGS0044', 'TEST002', 'gift_0001_10', 'gift_0001_50', 'DCGS0066N', 'gift_0001_30', 'PADS', 'ADJUST', 'gift_0001_40', 'gift_0001_60', 'gift_0001_70', 'gift_0001_90', 'DCGSSGIRL', 'DCGS0006', 'DCGS0016', 'DCGS0027', 'DCGS0036', 'DCGS0039', 'DCGS0060', 'DCGS0056', 'DCGS0059', 'GIFT', 'DCGSLBOY', 'm', 'DCGS0053', 'DCGS0062', 'DCGS0037', 'DCGSSBOY', 'DCGSLGIRL', 'S', 'DCGS0069', 'DCGS0070', 'DCGS0075', 'B', 'DCGS0041', 'ADJUST2', '47503J ', 'C3', 'SP1002', 'AMAZONFEE']`

This dataset really helped me refine my dataset analysis preparation skils and massively tickled the analyst and engineer inside of me (E.g., putting a system together to simplify data pre-processing on future projects).

You can find the full analysis with my raw thoughts at each step in the [analysis.ipynb](/analysis.ipynb) Jupyter Notebook.

What you'll find in the notebook:

- Initial Exploratory Data Analysis (EDA)
- Handling of missing values and invalid records
- Feature Engineering
- K-Means Clustering

## Extensions

This dataset is very comprehensive and has a lot of flexibility for smaller analyses. Here's some examples:

- DCGS `StockCodes` - which one performed the best
- Identifying what items are mostly gifted
- Understanding more about the items that are missing Customer IDs. E.g., are they thefts or stock-write offs?

## Summary

Key points to action during data cleaning:

- Remove `A` record invoices
- Remove `Customer ID` missing values
