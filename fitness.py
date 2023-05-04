from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Please enter your gender(M/F)? ')
    birth_str =str( input('Please enter your birthday in this format: YYYY-MM-DD: '))
    lb = float(input('Please enter your weight in U.S. pounds: '))
    inches = float(input('Please enter your height in U.S. inches: '))
    kg = kg_from_lb(lb)
    cm = cm_from_in(inches)
    years =compute_age(birth_str) 
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    
    

    # Print the results for the user to see.
    print(f'Age (years):{years}\nWeight (kg):{kg:.2f}\nHeight (cm):{cm:.1f}\nBody mass index: {bmi:.1f}\nBasal metabolic rate (kcal/day): {bmr:.0f}')
#Age (years): 17
# Weight (kg): 65.77
# Height (cm): 147.3
# Body mass index: 30.3
# Basal metabolic rate (kcal/day): 1580

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = lb*0.453592
    return kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = inches*2.54
    return cm


def body_mass_index(kg, cm):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi= (kg/cm**2)*10000
    return bmi


def basal_metabolic_rate(gender, kg, cm, years):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    
    if gender.upper() == 'M':
        bmr =  88.362+(13.397*kg)+(4.799*cm)-(5.677*years)
        return bmr

    else:
        bmr = 447.593+(9.247*kg)+(3.098*cm)-(4.330*years)
        return bmr



# Call the main function so that
# this program will start executing.

main()