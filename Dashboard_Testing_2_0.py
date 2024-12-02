
    # Main title
    st.title("Control Dashboard")
    
    # Project number input
    project_number = st.text_input(
        label="Project Number",  # Provide a non-empty label
        value="",  # Default value
        placeholder="Enter Project Number",  # Placeholder text
        key="project_search",  # Key for session state tracking
        label_visibility="collapsed"  # Hide the label from the UI
    )
    if project_number:
        st.session_state.project_number = project_number  # Update session state with input
    
    # Tabs using streamlit_shadcn_ui
    tab = ui.tabs(
        options=['Setup Phase', 'Baseline', 'Processing – Update', 'Re-Baseline', 'S-Curves'],
        default_value='Setup Phase',
        key="Main"
    )
    
    # Add content to the tabs
    if tab == 'Setup Phase':
        st.subheader("Setup Phase")
        st.write("Inhalte für Setup Phase einfügen.")
        
    elif tab == 'Baseline':
        st.subheader("Baseline")
        tab_Baseline = ui.tabs(
            options=['Weights for baseline', "Calculation of the progress baseline"],
            default_value='Weights for baseline',
            key="Baseline"
        )
        if tab_Baseline == "Weights for baseline":
            st.write("Weights for baseline")
            con = get_sql_server_connection()
            con2 = get_mysql_connection()
        
    elif tab == 'Processing – Update':
        st.subheader("Processing – Update")
        st.write("Inhalte für Processing – Update einfügen.")
        
    elif tab == 'Re-Baseline':
        st.subheader("Re-Baseline")
        st.write("Inhalte für Re-Baseline einfügen.")
        
    elif tab == 'S-Curves':
        st.subheader("S-Curves")
        st.write("Inhalte für S-Curves einfügen.")
    
    # Debugging output to show the project number entered
    st.write(f"Selected Project Number: {st.session_state.get('project_number', 'Not set')}")

# Main function call
Main()




