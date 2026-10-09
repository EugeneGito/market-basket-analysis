# Market Basket Analysis: What Do Customers Buy Together?

An association rule mining project on UK online retail transactions, using Python, the Apriori algorithm and `mlxtend`. The goal is to find which products are bought together and turn those patterns into practical recommendations on bundling, stocking and merchandising.

**Author:** Eugene Gitonga
**Tools:** Python, pandas, mlxtend, matplotlib, seaborn
**Notebook:** [`market\_basket\_analysis.ipynb`](./market_basket_analysis.ipynb) <!-- rename to match your file -->

\---

## Business Question

> Which products tend to be purchased together, and how can those associations be used to improve cross-selling, product bundling, stock planning and store layout?

## Dataset

Transaction records from a UK-based online gift retailer, covering December 2010 to December 2011. Each row is one line item on an invoice.

|Column|Description|
|-|-|
|InvoiceNo|Unique transaction identifier (a leading "C" marks a cancellation)|
|StockCode|Unique product code|
|Description|Product name|
|Quantity|Units purchased|
|InvoiceDate|Date and time of the transaction|
|UnitPrice|Price per unit|
|CustomerID|Customer identifier (where available)|
|Country|Country where the transaction took place|

Source: Online Retail dataset Kaggle. <https://www.kaggle.com/datasets/thedevastator/online-retail-sales-and-customer-data>

## Approach

1. **Cleaning** (chained pandas pipeline)

   * Converted `InvoiceDate` to a datetime type
   * Removed rows with zero or negative quantity or price
   * Removed cancelled invoices
   * Removed non-product stock codes (pure-letter codes such as postage and manual adjustments)
   * Trimmed whitespace in invoice, stock code and description columns
   * Assigned the most frequent description to each stock code
2. **Scope:** filtered to UK orders, so regional buying habits don't create artificial associations.
3. **Basket preparation:** grouped products by invoice into a list of lists, then one-hot encoded with `TransactionEncoder`.
4. **Mining:** ran Apriori with `min\_support = 0.01`, then generated rules with a minimum confidence of 0.8. This produced **181 rules**, and only **5** at a support of 2% or more.
5. **Removing redundancy:** many rules were the same itemset written in both directions. Keeping one rule per itemset left **94 unique rules**.
6. **Grouping into product families** by keyword, then summarising confidence, lift and support per family.
7. **Seasonality check:** plotted the monthly share of orders containing each family.
8. **Baseline popularity check:** compared individual item support to separate genuine associations from simple bestsellers.

## Key Findings

|Family|Rules|Avg confidence|Avg lift|Pattern|
|-|-|-|-|-|
|Herb markers|26|92%|71|Buyers of two or three herb markers almost always buy the full set|
|Jumbo bags|27|84%|8.1|Nearly every rule ends in Jumbo Bag Red Retrospot|
|Charlotte bags|23|85%|16.9|Designs combine and end in Red Retrospot Charlotte Bag|
|Regency teacups|7|86%|16.5|Pink, Roses and Green teacups bought as a set|
|Regency tea plates|4|89%|44.9|Same Pink, Roses, Green pattern as the teacups|
|Other sets|7|83% to 90%|10 to 40|Christmas wooden decorations, sweets bowls, Poppy's Playhouse, paper party ware|

1. **Customers buy ranges, not individual products.** Almost every strong rule stays inside one product family, and many extend across a shared design theme such as Red Retrospot.
2. **The Regency teacup set is the most commercially important pattern.** Customers who buy the Pink and Roses teacups buy the Green one 90% of the time (2.75% of all orders). Pink alone leads to Green 82% of the time, at the highest support of any rule (3.22%).
3. **Green pieces complete the sets.** Green is the consequent in both the teacup and tea plate rules, yet green teacups appear in only about 5% of orders. They are not a bestseller. They are the piece customers add to finish a set.
4. **Jumbo bag rules are strong but less informative.** Jumbo Bag Red Retrospot appears in about 11% of orders, so high confidence is partly expected.
5. **Several families are seasonal.** Christmas wooden decorations are near zero until August and peak at about 11% of orders in November. Herb markers peak in June (3.2%) and fall to about 0.5% by October. Charlotte bags and party ware are strongest in summer.

## Recommendations

1. **Bundle the sets.** Offer the herb marker set, the Regency teacup trio and the tea plate trio as ready-made bundles.
2. **Protect the set-completing items.** Keep the Green teacup, Green tea plate and Red Retrospot Charlotte and jumbo bags continuously in stock, since a stock-out can break a set purchase. (This is an inference. The data contains no inventory records.)
3. **Merchandise by range.** Create dedicated "Regency", "Jumbo bag" and "Retrospot" sections in store and online.
4. **Plan stock and promotions on a seasonal calendar.**

   * Christmas wooden decorations: stock from August, promote from September
   * Herb markers: stock in January and February for a February to June peak
   * Charlotte bags and party ware: promote from January to August
5. **Use the rules for cross-selling.** Show "customers also bought" suggestions based on the strongest rules.

## Limitations

* **Thresholds shape the findings.** Minimum support (1%) and minimum confidence (80%) mean every rule meets those levels by construction. Rarer patterns below 1% were not examined.
* **Lift is hard to compare across families.** The maximum possible lift depends on how rare the consequent is, so rare items such as herb markers show very high lift. Confidence and support are fairer comparisons across families.
* **One year of data.** Seasonal patterns can't be separated from trend or product changes. Regency tea plates first appear in May 2011, so their rules rest on about seven months of sales.
* **Customer mix.** This retailer sells to many wholesale buyers, so baskets may reflect trade customers restocking sets rather than individual shoppers.
* **Scope and causation.** The analysis covers UK orders only, and association does not prove that one purchase causes another.

## Next Steps

* Validate the bundle and range recommendations with an A/B test
* Repeat with a lower support threshold using FP-Growth to find rarer patterns
* Add margin data so recommendations can be ranked by profit, not frequency

Extend the analysis to other countries or a second year of data



Contact

Eugene Gitonga
Portfolio: https://datascienceportfol.io/eugeneigitonga
X: https://x.com/GITONGAeugene

