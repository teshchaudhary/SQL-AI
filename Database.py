import streamlit as st
import mysql.connector
from streamlit_extras.add_vertical_space import add_vertical_space

with st.sidebar:
    st.title('SQL - AI')
    st.markdown('''
    ## These are some Links
    - [GitHub Repository](https://github.com/teshchaudhary/Chat-PDF-App)     
    - [GitHub](https://github.com/teshchaudhary)
    - [LinkedIn](https://www.linkedin.com/in/tesh-chaudhary/)
    ''')
    add_vertical_space(5)
    # Works as a print function of Python
    st.write('Made by Tesh Chaudhary')

# Create a connection to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your database host
            user="root",       # Replace with your database username
            passwd="Tesh@1234",  # Replace with your database password
            database="classicmodels"  # Replace with the name of your database
        )
        return connection
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

# Streamlit app
st.title("Query-App")

# Connect to the database
connection = connect_to_database()

if connection:
    st.success("Connected to the MySQL database")

    # Create a cursor
    cursor = connection.cursor()

    # Custom SQL query input
    custom_query = st.text_input("Enter a SQL query:")
    if st.button("Execute Query"):
        cursor.execute(custom_query)
        results = cursor.fetchall()
        st.write("Query result:")

        if results:
            col_names = [i[0] for i in cursor.description]
            st.table([col_names] + results)
        
        # Non tabular format
        # for row in results:
        #     st.write(row)

    # Close the cursor and connection when done
    cursor.close()
    connection.close()
else:
    st.error("Failed to connect to the database")

if st.button("Reconnect"):
    connection = connect_to_database()


# To run the Streamlit app
if __name__ == "__main__":
    st.write("Made by Tesh Chaudhary")
