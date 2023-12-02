import gradio as gr
from ques_1 import driver1
from ques_2 import driver2

q1 = gr.Interface(
    fn=driver1,
    inputs=gr.Textbox(
        label="Enter your industry to know more about the customers that use salesforce: ",
        info="Food, Health care, Sports, etc...",
        lines=1,
    ),
    outputs="text",
)

q2 = gr.Interface(
    fn=driver2,
    inputs=gr.Textbox(
        label="Enter your customer to know more about how they leverage salesforce",
        info="Williams-Sonoma Inc., ReserveBar, Christy Sports, etc...",
        lines=1,
    ),
    outputs="text",
)

app = gr.TabbedInterface([q1, q2], ["Industry based Customers", "Customer stories leveraging Salesforce"])

if __name__ == "__main__":
    app.launch()
