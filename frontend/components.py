import streamlit as st


def hero():

    st.title("📄 ContractIQ")

    st.caption("AI Powered Employment Contract Analyzer")

    st.divider()


def metrics(report):

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Risk Score",
            report["risk_score"]
        )

    with c2:
        st.metric(
            "Risk Level",
            report["risk_level"]
        )

    with c3:
        st.metric(
            "Clauses",
            len(report["clauses"])
        )


def summary(report):

    st.subheader("Summary")

    st.info(report["summary"])


def clauses(report):

    st.subheader("Clause Analysis")

    for clause in report["clauses"]:

        with st.expander(clause["title"]):

            st.write("### Clause")

            st.write(clause["clause"])

            st.write("### Meaning")

            st.write(clause["analysis"]["meaning"])

            st.write("### Risk")

            st.write(clause["analysis"]["classification"])

            st.write("### Explanation")

            st.write(clause["analysis"]["explanation"])

            st.write("### Negotiation Tip")

            st.success(
                clause["analysis"]["negotiation_tip"]
            )