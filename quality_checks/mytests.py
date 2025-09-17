from dataqualitychecks import check_for_nulls
from dataqualitychecks import check_for_min_max
from dataqualitychecks import check_for_valid_values
from dataqualitychecks import check_for_duplicates

test1={
	"testname": "Check for nulls",
	"test": check_for_nulls,
	"table": "dimdate",
	"column": "dateid"
}

test2={
	"testname": "Check for DimDate.month in [1..12]",
	"test": check_for_min_max,
	"table": "dimdate",
	"column": "Month",
	"minimum": 1,
	"maximum": 12
}

test3={
	"testname": "Check for DimDate.quartername in {Q1..Q4}",
	"test": check_for_valid_values,
	"table": "dimdate",
	"column": "QuarterName",
	"valid_values": {'Q1','Q2','Q3','Q4'}
}

test4={
	"testname": "Check for DimProduct.productid unique",
	"test": check_for_duplicates,
	"table": "dimproduct",
	"column": "Productid"
}
