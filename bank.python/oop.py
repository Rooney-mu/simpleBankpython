from bankaccount import *
john=bank(1000,'john')
prince=bank(2000,'prince')

john.deposit(1000)
prince.deposit(2000)

john.withdraws(500)
prince.withdraws(1000)

john.saving(1000,"education")
prince.saving(1000,"lunch")

john.send(600)
prince.send(600)


john.intrests()
prince.intrests()


