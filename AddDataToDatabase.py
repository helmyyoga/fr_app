import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://teha-27d7f-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference ('Member')

data = {
"23051001":
    {
        "name": "ONIK",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "2",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051002":
    {
        "name": "HELMY",
        "stages": "INTERMEDIATE",
        "starting_year":2023,
        "total_attendance":0,
        "level": "5",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051003":
    {
        "name": "ALI",
        "stages": "INTERMEDIATE",
        "starting_year":2023,
        "total_attendance":0,
        "level": "5",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051004":
    {
        "name": "RIDHA",
        "stages": "INTERMEDIATE",
        "starting_year":2023,
        "total_attendance":0,
        "level": "4",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051005":
    {
        "name": "DOVI",
        "stages": "INTERMEDIATE",
        "starting_year":2023,
        "total_attendance":0,
        "level": "5",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051006":
    {
        "name": "FIKRI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051007":
    {
        "name": "VIKTOR",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051008":
    {
        "name": "RIFKI",
        "stages": "ADVANCE",
        "starting_year":2023,
        "total_attendance":0,
        "level": "6",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051009":
    {
        "name": "ANAS",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051010":
    {
        "name": "DIXXIELAND",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051011":
    {
        "name": "CORY",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051012":
    {
        "name": "NOVI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051013":
    {
        "name": "EMMA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051014":
    {
        "name": "EVA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051015":
    {
        "name": "ALFI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "2",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051016":
    {
        "name": "AZIZ",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "3",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051017":
    {
        "name": "DWI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051018":
    {
        "name": "WIWI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23051019":
    {
        "name": "NADYA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23061020":
    {
        "name": "FARIZ",
        "stages": "INTERMEDIATE",
        "starting_year":2023,
        "total_attendance":0,
        "level": "4",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23061021":
    {
        "name": "KALYA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23061022":
    {
        "name": "INCA R",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23061023":
    {
        "name": "TIKA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23061024":
    {
        "name": "DIRA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23061025":
    {
        "name": "GITA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23061026":
    {
        "name": "ICHA Y",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23061027":
    {
        "name": "ICHA N",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23061028":
    {
        "name": "MEY",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071029":
    {
        "name": "AUDY",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071030":
    {
        "name": "IDHAM",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071031":
    {
        "name": "KORI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071032":
    {
        "name": "TARI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071033":
    {
        "name": "ARIE",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071034":
    {
        "name": "RIFKHA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071035":
    {
        "name": "RONA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "2",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071036":
    {
        "name": "ADRIANO GULTOM",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071037":
    {
        "name": "GIAR",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071038":
    {
        "name": "RAMA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071039":
    {
        "name": "KRISHNAWD",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071040":
    {
        "name": "CAHYADI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071041":
    {
        "name": "SONY",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071042":
    {
        "name": "LUTHFI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23071043":
    {
        "name": "TITHA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081044":
    {
        "name": "MELLY",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081045":
    {
        "name": "DEE",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081046":
    {
        "name": "YOGA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "2",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081047":
    {
        "name": "ADEL",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081048":
    {
        "name": "CEL",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081049":
    {
        "name": "BILLY",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081050":
    {
        "name": "VEVA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081051":
    {
        "name": "SANTI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "2",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081052":
    {
        "name": "PUTRI",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081053":
    {
        "name": "DEPHE - RIAN",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081054":
    {
        "name": "RIRIE",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081055":
    {
        "name": "NIKITA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "1",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081056":
    {
        "name": "SHELLA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081057":
    {
        "name": "FRIEDA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    },
"23081058":
    {
        "name": "CANDRA",
        "stages": "BEGINNER",
        "starting_year":2023,
        "total_attendance":0,
        "level": "0",
        "ig": "ADA",
        "last_attendance_time": "2023-08-12 00:54:34"  
    }
}

for key,value in data.items():
    ref.child(key).set(value)