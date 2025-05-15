document.addEventListener('DOMContentLoaded', function() {
    const csvFileInput = document.getElementById('csvFile');
    const generateBtn = document.getElementById('generateBtn');
    const statusDiv = document.getElementById('status');

    csvFileInput.addEventListener('change', function() {
        generateBtn.disabled = !this.files.length;
    });

    generateBtn.addEventListener('click', async function() {
        const file = csvFileInput.files[0];
        if (!file) return;

        try {
            statusDiv.textContent = 'Processing...';
            const text = await file.text();
            const data = parseCSV(text);
            const doc = generateDocx(data);
            saveDocx(doc, 'MCQ_Question_Bank.docx');
            statusDiv.textContent = 'Document generated successfully!';
        } catch (error) {
            statusDiv.textContent = 'Error: ' + error.message;
        }
    });
});

function parseCSV(text) {
    const lines = text.split('\n');
    const headers = lines[0].split(',').map(h => h.trim());
    const data = [];

    for (let i = 1; i < lines.length; i++) {
        if (!lines[i].trim()) continue;
        const values = lines[i].split(',').map(v => v.trim());
        const row = {};
        headers.forEach((header, index) => {
            row[header] = values[index];
        });
        data.push(row);
    }

    return data;
}

function generateDocx(data) {
    const { Document, Paragraph, TextRun, HeadingLevel, AlignmentType } = docx;
    const doc = new Document();

    // Add title
    doc.addSection({
        children: [
            new Paragraph({
                text: "MCQ Question Bank",
                heading: HeadingLevel.HEADING_1,
                alignment: AlignmentType.CENTER
            })
        ]
    });

    let questionNumber = 1;
    const subdomains = [...new Set(data.map(row => row['Sub-domain']))];

    subdomains.forEach(subdomain => {
        const subdomainQuestions = data.filter(row => row['Sub-domain'] === subdomain);
        
        subdomainQuestions.forEach(row => {
            doc.addSection({
                children: [
                    new Paragraph({
                        text: `Sub Domain – ${subdomain}`,
                        heading: HeadingLevel.HEADING_2
                    }),
                    new Paragraph({
                        text: `Complexity – ${row['Complexity'].charAt(0).toUpperCase() + row['Complexity'].slice(1)}`,
                        style: 'Intense Quote'
                    }),
                    new Paragraph({
                        text: `Q. ${questionNumber}) ${row['Question']}`
                    }),
                    new Paragraph({
                        text: `A) ${row['Choice1']}`
                    }),
                    new Paragraph({
                        text: `B) ${row['Choice2']}`
                    }),
                    new Paragraph({
                        text: `C) ${row['Choice3']}`
                    }),
                    new Paragraph({
                        text: `D) ${row['Choice4']}`
                    }),
                    new Paragraph({
                        text: ""
                    })
                ]
            });
            questionNumber++;
        });
    });

    return doc;
}

function saveDocx(doc, filename) {
    docx.Packer.toBlob(doc).then(blob => {
        saveAs(blob, filename);
    });
} 