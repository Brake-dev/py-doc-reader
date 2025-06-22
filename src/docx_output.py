from docx import Document
from structured_output import DocListSchema


def to_docx(doc_list: DocListSchema):
    document = Document("./docs/docx/template.docx")

    for topic in doc_list.topics:
        document.add_heading(topic.title, level=1)

        for question in topic.questions:
            document.add_paragraph(question)

    document.save("rfp_response.docx")
