import pyemvue

vue = pyemvue.PyEmVue()
vue.login(username='joshtmontalto@gmail.com', password='Gab233raq!', token_storage_file='keys.json')


devices =  vue.get_devices()

for device in devices:
    print(device.device_name)


customer = vue.get_customer_details("joshtmontalto@gmail.com")
print(customer.first_name ,customer.created_at,)