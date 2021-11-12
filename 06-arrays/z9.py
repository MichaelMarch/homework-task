def month(n):
    months = [
        "Styczeń", "Luty", "Marzec", "Kwiecień",
        "Maj", "Czerwiec", "Lipiec", "Sierpień",
        "Wrzesień", "Październik", "Listopad",
        "Grudzień"
    ]
    
    return months[n - 1] if months[n - 1:] else ""