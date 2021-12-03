from win10toast import ToastNotifier

def notification(city):
    toaster = ToastNotifier()

    toaster.show_toast("Kujdes",f"Ajri shume i ndotur ne {city}")
