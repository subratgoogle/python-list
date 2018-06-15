items = ['Agra', 'Mumbai', 'Delhi', 'Kolkata', 'Jaipur', 'Simla', 'Bengluru']
ss = "******************************"
print(ss)
html_str = "This is famous cities of INDIA "
print(html_str)
ss = "******************************"
print(ss)
for item in items:
    html_str = "{} \n".format(item)
    print(html_str)

sts = "Indian Hotel Rent/Month"
print(sts)
sp = "************************"
print(sp)

cast = {

    "Agra": "10000/Month",
"Mumbai": "15000/Month",
"Delhi": "30000/Month",
"Kolkata": "20000/Month",
"Jaipur": "34000/Month",
"Simla": "45000/Month",
"Bengluru": "55000/Month"
}
for key, value in cast.items():
    print("Place : {}  Rent : {}".format(key, value))
