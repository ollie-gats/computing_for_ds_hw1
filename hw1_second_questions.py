from collections import defaultdict

CVs = [{'user': 'john', 'jobs': ['analyst', 'engineer']},
        {'user': 'jane', 'jobs': ['finance', 'software']},
        {'user': 'james', 'jobs': ['data', 'software']},
        {'user': 'dan', 'jobs': ['finance', 'software']},
        {'user': 'harry', 'jobs': ['finance', 'software']}]



def has_experience_as(CVs: list, job_title: str) -> list:
    """Returns a list of people with experience in a specific job

    Args:
        CVs (list): A list of dicitonaries with information about each users experience
        job_title (str): The type of job you want to find people with experience with

    Returns:
        list: Names of all people woith experience in specified job
    """
    
    has_experience = []
    for person in CVs:
        if job_title in person['jobs']:
            has_experience.append(person['user'])
            
    return has_experience



def job_counts(CVs: list) -> dict:
    """Takes a list of CVs and returns the number of people that have experience in each job

    Args:
        CVs (list): A list of dicitonaries with information about each users experience

    Returns:
        dict: A dictionary with the number of people that have experience for each job
    """
    
    job_count = defaultdict(int)
    for person in CVs:
        for job in person['jobs']:
            job_count[job] += 1
            
    return dict(job_count)
            



def most_popular_job(CVs: list) -> tuple:
    """Takes a list of CVs and returns the most popular job along with the number of people 
        with that job experience.

    Args:
        CVs (list): A list of dicitonaries with information about each users experience

    Returns:
        tuple: The most popular job and the count of people with this experience
    """
    
    job_count = job_counts(CVs)
    most_popular = max(job_count, key=job_count.get)
    
    return (most_popular, job_count[most_popular])