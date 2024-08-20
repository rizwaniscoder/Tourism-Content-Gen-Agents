from crewai import Task
from textwrap import dedent

PRODUCT_WEBSITE = "https://australiatravelsafe.com"
PRODUCT_DETAILS = "Australia Travel Safe offers comprehensive safety information and travel tips for tourists exploring Australia. Our services include up-to-date safety alerts, travel itineraries, and guides to help ensure a safe and enjoyable journey."

class MarketingAnalysisTasks:
    def product_analysis(self, agent):
        return Task(
            description=dedent(f"""\
                Analyze the Australia Travel Safe website: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Focus on identifying unique features, benefits,
                and the overall narrative presented.

                Your final report should clearly articulate the
                product's key selling points, its market appeal,
                and suggestions for enhancement or positioning.
                Emphasize the aspects that make Australia Travel Safe stand out.

                Keep in mind, attention to detail is crucial for
                a comprehensive analysis. It's currently 2024.
            """),
            agent=agent,
            expected_output=dedent("""\
                A comprehensive report detailing the unique features, benefits,
                and overall narrative of Australia Travel Safe, including key
                selling points, market appeal, and suggestions for enhancement
                or positioning.
            """)
        )

    def competitor_analysis(self, agent):
        return Task(
            description=dedent(f"""\
                Explore competitors of Australia Travel Safe: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Identify the top 3 competitors and analyze their
                strategies, market positioning, and customer perception.

                Your final report MUST include BOTH all context about {PRODUCT_WEBSITE}
                and a detailed comparison to the identified competitors.
            """),
            agent=agent,
            expected_output=dedent("""\
                A detailed analysis of the top 3 competitors of Australia Travel Safe,
                including their strategies, market positioning, and customer perception.
                The report should include a comparison with Australia Travel Safe.
            """)
        )

    def campaign_development(self, agent, platform, tone, audience):
        return Task(
            description=dedent(f"""\
                Develop a targeted marketing campaign for Australia Travel Safe: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Platform: {platform}
                Tone of Voice: {tone}
                Target Audience: {audience}

                Create a strategy and creative content ideas
                meticulously designed to captivate and engage
                the target audience.

                Based on your ideas, your co-workers will create the content for the campaign.

                Your final answer MUST include ideas that will resonate with the audience and
                all context you have about Australia Travel Safe.
            """),
            agent=agent,
            expected_output=dedent("""\
                A comprehensive marketing campaign strategy, including creative content ideas
                that resonate with the target audience and utilize all available context about
                Australia Travel Safe.
            """)
        )

    def instagram_ad_copy(self, agent, keywords):
        return Task(
            description=dedent(f"""\
                Craft engaging Instagram post copy for Australia Travel Safe.
                The copy should be punchy, captivating, concise,
                and aligned with the marketing strategy.

                Keywords: {keywords}

                Focus on creating a message that resonates with
                the target audience and highlights the unique
                selling points of Australia Travel Safe.

                Your ad copy must be attention-grabbing and should
                encourage viewers to take action, whether it's
                visiting the website, making a purchase, or learning
                more about the product.

                Your final answer MUST be 3 options for an ad copy for Instagram that
                not only informs but also excites and persuades the audience.
            """),
            agent=agent,
            expected_output=dedent("""\
                Three punchy, captivating, and concise Instagram ad copies that highlight
                the unique selling points of Australia Travel Safe and encourage viewers
                to take action.
            """)
        )

    def take_photograph_task(self, agent, copy, style):
        return Task(
            description=dedent(f"""\
                Take the most amazing photo ever for an Instagram post
                regarding Australia Travel Safe. Use the following copy:
                {copy}

                This is the product you are working with: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Image Style: {style}

                Imagine what the photo should look like and describe it in a paragraph.
                Here are some examples to follow:
                - a serene beach at sunrise with crystal clear waters, soft lighting, 4k, crisp
                - a hiker standing at the edge of a cliff overlooking a vast landscape, dramatic lighting, 4k, crisp
                - a close-up of native wildlife in their natural habitat, vibrant colors, 4k, crisp

                Think creatively and focus on how the image can capture the audience's
                attention. Don't show the actual product in the photo.

                Your final answer must be 3 options of photographs, each with 1 paragraph
                describing the photograph exactly like the examples provided above.
            """),
            agent=agent,
            expected_output=dedent("""\
                Three imaginative descriptions of potential Instagram photographs,
                each capturing a different aspect of Australia and aligning with the provided examples.
            """)
        )

    def review_photo(self, agent):
        return Task(
            description=dedent(f"""\
                Review the photos taken for Australia Travel Safe.
                Ensure they are the best possible and aligned with the product's goals.
                Review, approve, ask clarifying questions, or delegate follow-up work if necessary.

                This is the product you are working with: {PRODUCT_WEBSITE}.
                Extra details provided by the company: {PRODUCT_DETAILS}.

                Here are some examples of how the final photographs should look:
                - a serene beach at sunrise with crystal clear waters, soft lighting, 4k, crisp
                - a hiker standing at the edge of a cliff overlooking a vast landscape, dramatic lighting, 4k, crisp
                - a close-up of native wildlife in their natural habitat, vibrant colors, 4k, crisp

                Your final answer must be 3 reviewed options of photographs,
                each with 1 paragraph description following the examples provided above.
            """),
            agent=agent,
            expected_output=dedent("""\
                Three reviewed photograph descriptions, ensuring each aligns with Australia Travel Safe's goals
                and matches the provided examples.
            """)
        )
