"""Shared content for every theme. Sourced from rickybrockamp.com (About, Work,
Process, Photo, resume PDF) and the Concept Lab copy."""

NAME = "Ricky Brockamp"
ROLE = "Product Designer · Design Lead"
LOCATION = "Los Angeles, CA"
EMAIL = "rbrockamp1@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/rickybrockamp"
TAGLINE = "Leading product design for complex, regulated systems. Empathetic, solutions-oriented, persistent."
FOCUS = ["Design Systems", "Accessibility", "Research", "AI initiatives", "Product Strategy"]

BIO = [
    "Ricky is a leader in the product design space based in Los Angeles, with a diverse background that spans Fortune 500 companies and high-growth startups.",
    "He has found that the best way to serve the people affected by design is to stay empathetic, solutions-oriented, and persistent.",
    "Every project Ricky works on is shaped by his desire to solve deeply rooted and pressing societal issues. He believes research and design are compelling avenues for change.",
    "He works across a wide range of design challenges, from leading teams through complex problems to establishing design systems with cross-functional partners. Whether he’s talking with developers or strategizing with marketing directors, he brings a professionalism and positivity that leaves a lasting impact.",
]
OUTSIDE = "Outside of work, Ricky backpacks and fly fishes the Sierras with friends, takes road trips through the Southwest, and forages for wild mushrooms. His love of new experiences and building relationships carries into the work he puts into the world."

CASES = [
    dict(
        slug="nmls", n="01", title="NMLS Modernization", short="NMLS",
        kicker="Information Architecture", client="FINRA · Agency project",
        summary="A multiyear contract to modernize the NMLS platform.",
        img="nmls.jpg",
        alt="Laptop on a wooden desk showing the redesigned NMLS home screen with license status, quick links and an individual task list.",
        services=["Requirement gathering", "Design thinking workshops", "Information architecture", "End-to-end product design", "Promotional material"],
        overview=[
            "NMLS is the system of record that licensing professionals and regulators rely on. As part of a multiyear agency engagement with FINRA, Ricky helped modernize the platform from the ground up.",
            "The work started with the structure: understanding how people actually move through licensing tasks, and reshaping the navigation and information architecture so the most common jobs are the easiest to find.",
        ],
        did=[
            ("Requirement gathering", "Worked with stakeholders and end users to pull clear requirements out of a complex, regulated domain."),
            ("Design thinking workshops", "Facilitated workshops that aligned business, product and engineering partners on problems before solutions."),
            ("Information architecture", "Restructured navigation so license status, quick links and open tasks sit together on one home screen."),
            ("End-to-end product design", "Carried the work from task flows and wireframes through high-fidelity, developer-ready designs."),
            ("Promotional material", "Produced material that helped introduce the modernized experience to its audience."),
        ],
    ),
    dict(
        slug="finra-ui", n="02", title="Design System — FINRA UI", short="FINRA UI",
        kicker="Design System & Accessibility", client="FINRA",
        summary="Moving a design system from Adobe XD to Figma, and the team with it.",
        img="design-system.jpg",
        alt="Laptop showing the FINRA UI design system site, with navigation for colors, typography, spacing, icons and components.",
        services=["Design systems", "Figma migration", "Theming", "Accessibility", "Training & curriculum", "Governance"],
        overview=[
            "Product design and design systems work that included FINRA’s transition from Adobe XD to Figma, a massive effort across the organization.",
            "Ricky took a leading role in the collaboration, assembling a team of volunteers who rebuilt every component using modern techniques and deep Figma knowledge.",
        ],
        did=[
            ("Led the migration", "Coordinated the move of the full component library from Adobe XD to Figma."),
            ("Built a volunteer team", "Assembled designers who rebuilt all components with modern Figma techniques."),
            ("Upskilled 20+ designers", "Created the curriculum and training program that brought the design team up to speed."),
            ("Extended through theming", "Added theming that supports a partner brand and accessibility features like dark mode."),
            ("Set up governance", "Established design governance so the system stays consistent as it grows."),
        ],
    ),
    dict(
        slug="regulator-workspace", n="03", title="Regulator Workspace", short="Regulator Workspace",
        kicker="Product Design · FINRA client", client="FINRA · Key client",
        summary="Enterprise software for financial supervision, rebuilt around the people who use it.",
        img="regulator-workspace.jpg",
        alt="Laptop showing an Individual Profile screen with search and cards for blank forms, CRD fee schedule, web browsers, FAQs, IARD fee schedule and contact support.",
        services=["Product design", "Stakeholder management", "Validation", "Enterprise UX"],
        overview=[
            "Product design work for a key client in financial supervision. The engagement began with a trust gap between the client and the delivery team.",
            "Ricky restored that trust through diligent communication and collaboration, internally and externally, while improving bespoke enterprise software for the regulators who use it every day.",
        ],
        did=[
            ("Restored trust", "Rebuilt the working relationship through clear, consistent communication with the client and internal partners."),
            ("Validated often", "Kept frequent touchpoints with users to check each change against real workflows."),
            ("Championed the customer", "Advocated for the customer’s voice and for solutions that improve their workflow, in the face of many hurdles."),
            ("Simplified the entry points", "Brought common resources such as forms, fee schedules and support into one clear starting screen."),
        ],
    ),
    dict(
        slug="real-estate-tech", n="04", title="Real Estate Tech", short="Real Estate Tech",
        kicker="Branding & Product Design", client="Returning client",
        summary="Rebuilding trust with a returning client by redesigning a legacy experience.",
        img="real-estate.jpg",
        alt="Desktop monitor showing a sign-in screen for ARG Corp. with username and password fields beside a photo of a person smiling at a laptop.",
        services=["Branding", "Product design", "Workshops", "Cross-functional collaboration"],
        overview=[
            "A product design and branding project for a returning client, focused on rebuilding trust by redesigning a legacy experience with a modern, ergonomic user experience.",
            "The team facilitated engaging workshops, collaborated across functions and delivered high-quality work at a lightning-fast pace.",
        ],
        did=[
            ("Rebuilt trust", "Re-established the relationship with a returning client through transparent, collaborative work."),
            ("Refreshed the brand", "Gave the product a modern identity, carried through into the interface."),
            ("Redesigned the legacy experience", "Replaced dated flows with a modern, ergonomic experience, starting at sign-in."),
            ("Ran workshops", "Facilitated workshops that kept stakeholders engaged and decisions moving quickly."),
        ],
    ),
]

TESTIMONIALS = [
    dict(name="Brooke Davidson Hoareau", role="Associate Director of UX, FINRA", quote=[
        "It has been a privilege to manage Ricky as a Product Designer for FINRA. From the beginning Ricky demonstrated his exceptional leadership skills. He partners well with stakeholders, product managers, engineers, and business partners with his transparent and friendly demeanor. He supports a positive design community and goes above and beyond to help better the organization and advocate for UX.",
        "Ricky is a thoughtful mentor, a gifted designer, and an inspiring leader. Ricky’s enthusiasm is contagious; many positive workplace initiatives were initiated or inspired by him, including our meditation practice and low-fi working sessions that combat isolation, boost morale and support team members.",
        "Ricky is a talented professional and would be an invaluable asset to any organization. I would gladly work with Ricky again.",
    ]),
    dict(name="Keely Funkhouser", role="VP Product, Randall Reilly", quote=[
        "Ricky is very easy to work with, very responsive, and efficient with his time. He not only follows through with deliverables, but he also trains the people he collaborates with as he goes, adding more value to his engagements than expected.",
    ]),
    dict(name="Jasmine Nehzati", role="Experience Designer, Team One", quote=[
        "Ricky has a great understanding of scope and his designs are always thoughtful, empathetic, and impactful. Ricky is the go-to designer when gaining perspective on improving designs due to his great attention to detail and problem-solving ability.",
    ]),
]

PROCESS = [
    dict(n="01", title="Discovery", methods=["Active listening", "Persona creation", "Problem framing", "Extracting requirements", "Goal-oriented research"],
         text=["Every project starts with active listening. An effective solution depends on understanding the root problem, so this phase is about clear communication with end users and real insight into their needs, the business requirements and any unique circumstances.",
               "Key questions: who are the users, what do they assume, what do they need, how do they use existing products today, and what are they ultimately trying to achieve?"]),
    dict(n="02", title="Analysis & Planning", methods=["Stakeholder interviews", "Heuristic evaluations", "UX audits", "User journey mapping", "Market analysis"],
         text=["With the problem understood, the focus shifts to competitive and comparative research: exploring the landscape, identifying best-in-class patterns, and drawing on first-party data, previous research and known user sentiment.",
               "Then the creative work begins: bringing ideas to life, mapping task flows and building prototypes that bridge conceptual thinking and tangible design."]),
    dict(n="03", title="Cross-functional Collaboration", methods=["Documentation", "Training", "Progress updates", "Workshops"],
         text=["Engaging stakeholders, users, developers and business partners is ongoing. Regular meetings, asynchronous collaboration and progress reports keep everyone informed, and conflicting direction gets clarified in the moment to reduce the risk of misalignment.",
               "Keeping user needs at the front of an aligned roadmap keeps the design user-focused, meets business objectives and builds trust and transparency across the team."]),
    dict(n="04", title="Design, Validate, Iterate", methods=["Low & high fidelity wireframing", "Rapid prototyping", "Storyboarding", "Visual design", "UI creation", "Design systems", "Developer handoff"],
         text=["Ideation works best when several directions are explored before one is chosen. Rough concepts become low-fidelity wireframes; feedback drives the next iteration in medium or high fidelity.",
               "Where a design system exists, its components and patterns keep the work consistent. Files are prepared for handoff with correct build specs, clearly explained interactions and complete accessibility documentation."]),
    dict(n="05", title="Measure Success", methods=["Usability testing", "Net Promoter Score", "Engagement metrics", "Task completion time", "Benchmarking", "Qualitative insights"],
         text=["Surveys and user interviews validate the design direction. KPIs like Net Promoter Score, behavioral metrics such as time to complete a task, support call reduction and even revenue show whether a solution is working."]),
]

PHOTO_INTRO = "What I love about film is the anticipation and intention it requires. Every shot demands careful consideration of light, exposure, and composition, with no instant results — only the excitement of discovery. The raw grain and imperfections add depth, making each image feel organic and unfiltered. Even the mistakes become part of the story."
PHOTOS = [
    ("redwood-fog.jpg", "Fog drifting over a redwood forest above a golden meadow.", "l"),
    ("sea-cliff.jpg", "Black-and-white photo looking up a layered sea cliff that curves over dark water.", "p"),
    ("paris-cafe.jpg", "A burgundy Porsche 911 parked outside Le Vauban café, with red awnings and a man riding past on a bike.", "l"),
    ("cactus.jpg", "Black-and-white close-up of a clustered Pelecyphora aselliformis cactus with a botanical garden label.", "p"),
    ("market.jpg", "A woman in glasses smiling beside a shopping cart in a grocery store’s produce aisle.", "l"),
    ("golden-gate.jpg", "Black-and-white photo of the Golden Gate Bridge from the beach under streaked clouds.", "l"),
    ("flowers.jpg", "Black-and-white photo of a dense bed of small daisy-like flowers.", "p"),
    ("cornfield.jpg", "Tall corn stalks behind a strip of wildflowers under an overcast sky.", "l"),
    ("dinner.jpg", "A dinner table with a bowl topped with bonito flakes, a clay pot of tofu and a glass of water.", "l"),
]

RESUME_SUMMARY = "Product designer who leads teams, drives design system adoption and streamlines cross-functional collaboration, with a focus on empowering teammates and building an inclusive design community."
JOBS = [
    dict(org="FINRA", title="Product Designer", dates="May 2022 – Present", bullets=[
        "Lead product design from discovery to launch across 70+ enterprise applications.",
        "Led the design system migration from Adobe XD to Figma, built a training and upskilling program, and established design governance.",
        "Lead AI initiatives, including a cross-organization AI learning community.",
        "Help build an inclusive, diverse design community and introduced rituals that improved cross-functional collaboration.",
    ]),
    dict(org="Hexagon", title="Product Designer", dates="Oct 2021 – May 2022", bullets=[
        "Partnered with UX and product stakeholders to bring applications and workflows up to UX standards.",
        "Established user research guidelines and a phased rollout that sped up iteration and improved stakeholder collaboration.",
    ]),
    dict(org="SkillPointe", title="Product Designer", dates="Oct 2020 – Oct 2021", bullets=[
        "Audited existing designs, modernized the brand and built a cohesive design system.",
        "Advocated for user testing, introduced a validation process and specialized in responsive mobile design.",
        "Worked with The Home Depot’s design team on sponsored pages and restructured key user flows and information architecture.",
    ]),
    dict(org="Freelance", title="Product Designer", dates="Aug 2020 – Present", bullets=[
        "Deliver end-to-end product design for startup clients, using research to guide design strategy.",
        "Partner with product management and engineering to launch products that meet user and business goals.",
    ]),
]
EDUCATION = [
    ("B.A., Anthropology & Human-Computer Interaction", "California State University Channel Islands", "2020"),
    ("UX Design Immersive Certificate", "General Assembly", "2020"),
]
SKILLS = ["Product design", "Interaction design", "Visual design", "UX & UI design", "Responsive design", "Design systems", "Accessibility", "UX research", "Information architecture", "Design thinking", "Interactive prototyping", "Low- to high-fidelity design", "Dashboards", "Financial software", "B2B & B2C", "Branding", "Typography", "Color theory", "Data analysis", "Storytelling", "Product management", "Leadership"]
TOOLS = ["Figma", "Adobe Creative Suite", "Miro", "UserTesting", "Jira", "Confluence", "InVision", "SPSS", "Microsoft Office", "ChatGPT"]
