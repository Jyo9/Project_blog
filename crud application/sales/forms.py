from django import forms
from .models import SalesData

region = ["Sub-Saharan Africa", "Europe", "Asia", "Middle East and North Africa", "Central America and the Caribbean", "Australia and Oceania", "North America"]
REGION = tuple([(val, val) for val in region])

country = ["Namibia", "Iceland", "Russia", "Moldova ", "Malta", "Indonesia", "Djibouti", "Greece", "Cameroon", "Nigeria", "Senegal", "Afghanistan", "India", "Lebanon", "Turkey", "Iraq", "Rwanda", "Ukraine", "Finland", "South Sudan", "Antigua and Barbuda ", "Kuwait", "United Kingdom", "Saint Kitts and Nevis ", "Saint Lucia", "Tunisia ", "Yemen", "Guinea", "Tuvalu", "South Korea", "San Marino", "Trinidad and Tobago", "Kosovo", "Hungary", "Botswana", "Serbia", "Guatemala", "United Arab Emirates", "Samoa ", "Bahrain", "Saint Vincent and the Grenadines", "Pakistan", "Poland", "Lithuania", "Sudan", "Portugal", "Fiji", "Tanzania", "Sao Tome and Principe", "Cape Verde", "Greenland", "Guinea-Bissau", "Georgia", "Jamaica", "Bulgaria", "Kazakhstan", "Grenada", "Honduras", "Mongolia", "Belize", "United States of America", "South Africa", "Austria", "Marshall Islands", "Sierra Leone", "Romania", "Malaysia", "New Zealand", "Mozambique", "Somalia", "Denmark", "Solomon Islands", "Vanuatu", "Singapore", "Luxembourg", "Australia", "Brunei", "Papua New Guinea", "Kyrgyzstan", "Chad", "Togo", "Mali", "Croatia", "Taiwan", "Barbados", "Equatorial Guinea", "Canada", "Eritrea", "Mexico", "Niger", "Madagascar", "Gabon", "El Salvador", "Sweden", "Angola", "Sri Lanka", "Cyprus", "Ethiopia", "Liberia", "Egypt", "Montenegro", "Nauru", "Kiribati", "Iran", "Democratic Republic of the Congo", "Vatican City", "North Korea", "Jordan", "Seychelles ", "France", "Mauritius ", "Cambodia", "Dominican Republic", "Tajikistan", "Netherlands", "Comoros", "The Bahamas", "Burundi", "Syria", "Estonia", "Bosnia and Herzegovina", "Tonga", "Zambia", "Morocco", "Monaco", "Lesotho", "The Gambia", "Germany", "Slovenia", "Benin", "Turkmenistan", "Maldives", "Laos", "Cuba", "Myanmar", "Malawi", "Nicaragua", "Ireland", "Mauritania", "Costa Rica", "Azerbaijan", "Saudi Arabia", "Latvia", "Belgium", "Switzerland", "Bhutan", "Italy", "Central African Republic", "Vietnam", "Panama", "Kenya", "Libya", "Algeria", "Belarus", "Japan", "Ghana", "Philippines", "Czech Republic", "China", "Liechtenstein", "Palau", "Macedonia", "Bangladesh", "Slovakia", "Swaziland", "Burkina Faso", "Uganda", "Spain", "Andorra", "Zimbabwe", "Uzbekistan", "Oman", "Dominica", "Cote d'Ivoire", "Albania", "Thailand", "Norway", "East Timor", "Federated States of Micronesia", "Israel", "Haiti", "Republic of the Congo", "Qatar", "Armenia", "Nepal"]
COUNTRY = tuple([(val, val) for val in country])

item_type = ["Household", "Baby Food", "Meat", "Cereal", "Cosmetics", "Fruits", "Vegetables", "Office Supplies", "Personal Care", "Beverages", "Snacks", "Clothes"]
ITEM_TYPE = tuple([(val, val) for val in item_type])

SALES_CHANNEL = (
    ("Online", "Online"),
    ("Offline", "Offline"),
)

ORDER_PRIORITY =( 
    ("M", "Medium"), 
    ("H", "High"), 
    ("L", "Low"), 
    ("C", "Cancel"),
)

class SalesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        self.fields['region'].widget = forms.Select(choices=REGION)
        self.fields['country'].widget = forms.Select(choices=COUNTRY)
        self.fields['item_type'].widget = forms.Select(choices=ITEM_TYPE)
        self.fields['sales_channel'].widget = forms.RadioSelect(choices=SALES_CHANNEL, )
        self.fields['order_priority'].widget = forms.Select(choices=ORDER_PRIORITY)
        self.fields['order_date'].widget = forms.DateInput(attrs={'type': 'date', 'required': True})
        self.fields['ship_date'].widget = forms.DateInput(attrs={'type': 'date', 'required': True})
        
        

    class Meta:
        model = SalesData
        fields = ('region', 'country', 'item_type', 'sales_channel', 'order_priority', 
                    'order_date', 'ship_date', 'units_sold', 'unit_price', 'unit_cost')
