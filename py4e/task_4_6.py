hrs = float(input("Enter Hours:"))
rph = float(input("Enter rate:"))


def computepay(hrs,rph):
    if hrs<40:
    	pay = hrs*rph
    if hrs>=40:
        virsstundas = hrs-40
        pamatalga = (hrs - virsstundas)*rph
        bonuss = (hrs-40)*(rph*1.5)
        pay = pamatalga + bonuss
        
        print("Pay",pay)
        return pay
p = computepay(hrs,rph)
