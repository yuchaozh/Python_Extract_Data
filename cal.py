page = 20120816;
while page <= 20130519:
	print page, "\n";
	page = page + 16;
	num = page % 100;
	numMonth = page % 10000;
	if num >= 40:
		page = page - 48 + 100;
	if numMonth >= 1300:
		page = page - 1300+ 10000;