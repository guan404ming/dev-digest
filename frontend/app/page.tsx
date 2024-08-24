import { BlogPosts } from "app/components/posts";
import { TextAnimate } from "./components/text-animate";

function Badge(props) {
  return (
    <a
      {...props}
      target="_blank"
      className="inline-flex items-center rounded border border-neutral-200 bg-neutral-50 p-1 text-sm leading-4 text-neutral-900 no-underline dark:border-neutral-700 dark:bg-neutral-800 dark:text-neutral-100"
    />
  );
}

const texts = [
  "an IM student 🧑‍🎓",
  "a web developer 🧑‍💻",
  "a open source enthusiast 🚀",
  "a tech lover ❤️‍🔥",
];

export default function Page() {
  return (
    <section className="space-y-4 flex-col">
      <TextAnimate text="Hey, I'm Wesley 👋" type="popIn" />

      {/* <div className="text-white rounded-2xl">
        <Typewriter texts={texts} delay={0.5} baseText="I'm " />
      </div> */}

      <p className="leading-7">
        {`I'm currently study information management at `}
        <span className="not-prose">
          <Badge href="https://www.ntu.edu.tw/">
            <img
              alt="Next.js logomark"
              src="/ntu.png"
              className="!mr-1"
              width="12"
              height="12"
            />
            NTU
          </Badge>
        </span>
        {`. I'm also a web developer & open source enthusiast. I have a deep passion for new technologies and love finding creative ways to solve complex challenges.`}
      </p>
      <div className="my-8">
        <BlogPosts />
      </div>
    </section>
  );
}
