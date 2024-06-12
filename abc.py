import streamlit as st

def calculate_simple_interest(principal, rate, time):
    """Calculate the simple interest"""
    return (principal * rate * time) / 100

def main():
    st.title("Simple Interest Calculator")

    st.sidebar.header("Input Parameters")
    
    principal = st.sidebar.number_input("Principal Amount", min_value=0.0, value=1000.0)
    rate = st.sidebar.number_input("Annual Interest Rate (%)", min_value=0.0, value=5.0)
    time = st.sidebar.number_input("Time (years)", min_value=0.0, value=1.0)
    
    if st.sidebar.button("Calculate"):
        interest = calculate_simple_interest(principal, rate, time)
        total_amount = principal + interest
        
        st.write(f"### Principal Amount: ${principal:.2f}")
        st.write(f"### Annual Interest Rate: {rate:.2f}%")
        st.write(f"### Time Period: {time:.2f} years")
        st.write(f"### Simple Interest: ${interest:.2f}")
        st.write(f"### Total Amount: ${total_amount:.2f}")

if __name__ == "__main__":
    main()
