import { BlogPosts } from "app/components/posts";
import { TextAnimate } from "./components/text-animate";

function Badge(props: React.ComponentProps<"a">) {
  return (
    <a
      {...props}
      target="_blank"
      className="inline-flex items-center rounded border border-neutral-200 bg-neutral-50 p-1 text-sm leading-4 text-neutral-900 no-underline dark:border-neutral-700 dark:bg-neutral-800 dark:text-neutral-100"
    />
  );
}

const texts = [
  "IM student",
  "web developer",
  "open source enthusiast",
  "tech lover ❤️",
];

export default function Page() {
  return (
    <section className="space-y-4 flex-col">
      <TextAnimate text="Hey, I'm Wesley 👋" type="popIn" />

      <div className="leading-7">
        {`I'm a junior at `}
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
        {` studying Information Management, a web developer, and an open-source enthusiast. I have a deep passion for exploring new tech and love finding creative solutions to complex challenges!`}
      </div>

      <div className="my-8">
        <BlogPosts />
      </div>
    </section>
  );
}
