def concatenate_data(personal_info, internship_projects):
    # Create a dictionary from the tuple
    internship_projects_dict = {f'Project_{i+1}': project for i, project in enumerate(internship_projects)}
    
    # Merge dictionaries
    combined_info = {**personal_info, **internship_projects_dict}
    
    return combined_info

# Dictionary containing personal information
personal_info = {
    'Name': 'Maasandram Murali',
    'Age': 19,
    'Email': 'muralimurali43792@gmail@gmail.com'
}

# Tuple containing internship and project details
internship_projects = (
    'Internship at IIDT (BlackBucks)',
    'Project on Embedded Developer',
    'Project on Web IoT'
)

# Call the function and print the result
combined_info = concatenate_data(personal_info, internship_projects)
print(combined_info)
