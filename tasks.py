from crewai import Task
from textwrap import dedent

PRODUCT_WEBSITE = "https://australiatravelsafe.com.au"
PRODUCT_DETAILS = "Australia Travel Safe offers comprehensive safety information and travel tips for tourists exploring Australia. Our services include up-to-date safety alerts, travel itineraries, and guides to help ensure a safe and enjoyable journey."

class MarketingAnalysisTasks:
    def product_analysis(self, agent, country):
        return Task(
            description=dedent(f"""\
                Analyze the {country} Travel Safe website: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Focus on identifying unique features, benefits, and the overall narrative presented.

                Your final report should clearly articulate the product's key selling points, its market appeal, and suggestions for enhancement or positioning.
                Emphasize the aspects that make {country} Travel Safe stand out.

                Keep in mind, attention to detail is crucial for a comprehensive analysis. It's currently 2024.
            """),
            agent=agent,
            expected_output=dedent(f"""\
                A comprehensive report detailing the unique features, benefits, and overall narrative of {country} Travel Safe, including key selling points, market appeal, and suggestions for enhancement or positioning.
            """)
        )

    def competitor_analysis(self, agent, country):
        return Task(
            description=dedent(f"""\
                Explore competitors of {country} Travel Safe: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Identify the top 3 competitors and analyze their strategies, market positioning, and customer perception.

                Your final report MUST include BOTH all context about {PRODUCT_WEBSITE} and a detailed comparison to the identified competitors in the {country} market.
            """),
            agent=agent,
            expected_output=dedent(f"""\
                A detailed analysis of the top 3 competitors of {country} Travel Safe, including their strategies, market positioning, and customer perception. The report should include a comparison with {country} Travel Safe.
            """)
        )

    def campaign_development(self, agent, platform, tone, audience, country):
        return Task(
            description=dedent(f"""\
                Develop a targeted marketing campaign for {country} Travel Safe: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Platform: {platform}
                Tone of Voice: {tone}
                Target Audience: {audience}

                Create a strategy and creative content ideas meticulously designed to captivate and engage the target audience in {country}.

                Based on your ideas, your co-workers will create the content for the campaign.

                Your final answer MUST include ideas that will resonate with the audience and all context you have about {country} Travel Safe.
            """),
            agent=agent,
            expected_output=dedent(f"""\
                A comprehensive marketing campaign strategy for {country}, including creative content ideas that resonate with the target audience and utilize all available context about {country} Travel Safe.
            """)
        )

    def instagram_ad_copy(self, agent, keywords, country):
        return Task(
            description=dedent(f"""\
                Craft engaging Instagram post copy for {country} Travel Safe.
                The copy should be punchy, captivating, concise, and aligned with the marketing strategy.

                Keywords: {keywords}

                Focus on creating a message that resonates with the target audience in {country} and highlights the unique selling points of {country} Travel Safe.

                Your ad copy must be attention-grabbing and should encourage viewers to take action, whether it's visiting the website, making a purchase, or learning more about the product.

                Your final answer MUST be 3 options for an ad copy for Instagram that not only informs but also excites and persuades the audience in {country}.
            """),
            agent=agent,
            expected_output=dedent(f"""\
                Three punchy, captivating, and concise Instagram ad copies that highlight the unique selling points of {country} Travel Safe and encourage viewers to take action.
            """)
        )

    def take_photograph_task(self, agent, copy, style, country):
        return Task(
            description=dedent(f"""\
                Take the most amazing photo ever for an Instagram post regarding {country} Travel Safe.
                Use the following copy: {copy}

                This is the product you are working with: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Image Style: {style}

                Imagine what the photo should look like and describe it in a paragraph.
                Here are some examples to follow:
                - a serene beach at sunrise in {country} with crystal clear waters, soft lighting, 4k, crisp
                - a hiker standing at the edge of a cliff in {country} overlooking a vast landscape, dramatic lighting, 4k, crisp
                - a close-up of native wildlife in their natural habitat in {country}, vibrant colors, 4k, crisp

                Your final answer must be 3 options of photographs, each with 1 paragraph describing the photograph exactly like the examples provided above.
            """),
            agent=agent,
            expected_output=dedent(f"""\
                Three imaginative descriptions of potential Instagram photographs in {country}, each capturing a different aspect and aligning with the provided examples.
            """)
        )

    def review_photo(self, agent, country):
        return Task(
            description=dedent(f"""\
                Review the photos taken for {country} Travel Safe.
                Ensure they are the best possible and aligned with the product's goals.
                Review, approve, ask clarifying questions, or delegate follow-up work if necessary.

                This is the product you are working with: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Here are some examples of how the final photographs should look:
                - a serene beach at sunrise in {country} with crystal clear waters, soft lighting, 4k, crisp
                - a hiker standing at the edge of a cliff in {country} overlooking a vast landscape, dramatic lighting, 4k, crisp
                - a close-up of native wildlife in their natural habitat in {country}, vibrant colors, 4k, crisp

                Your final answer must be 3 reviewed options of photographs, each with 1 paragraph description following the examples provided above.
            """),
            agent=agent,
            expected_output=dedent(f"""\
                Three reviewed photograph descriptions from {country}, ensuring each aligns with the goals of {country} Travel Safe and matches the provided examples.
            """)
        )