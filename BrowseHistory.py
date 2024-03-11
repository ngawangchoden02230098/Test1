from queue import LifoQueue

backward_histroy = LifoQueue()
forward_history = LifoQueue()
current_page = None

#Visit function
NoOfVisits = int(input("Enter the number of url hsotory: "))
print("Enter URLs to visits: ")
for i in range(NoOfVisits):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_histroy.put(current_page)
    current_page = url

# Display current page
print(f"Current_page: {current_page}")

# Go back
while input("Do you want to go back? (yes/no): ").lower() == 'yes' :
    if not backward_histroy.empty():
        forward_history.put(current_page)
        current_page = backward_histroy.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page available")

#Go forward
while input("Do you want to go forward? (yes/no): ").lower() == 'yes':
    if not forward_history.empty():
        backward_histroy.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward page available")