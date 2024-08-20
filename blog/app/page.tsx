import { BlogPosts } from "app/components/posts";

function Badge(props) {
  return (
    <a
      {...props}
      target="_blank"
      className="inline-flex items-center rounded border border-neutral-200 bg-neutral-50 p-1 text-sm leading-4 text-neutral-900 no-underline dark:border-neutral-700 dark:bg-neutral-800 dark:text-neutral-100"
    />
  );
}

export default function Page() {
  return (
    <section>
      <h1 className="mb-8 text-2xl font-semibold tracking-tighter">
        Hey, I'm Wesley 👋
      </h1>
      <p className="mb-4 leading-7">
        {`I'm a web developer & open source enthusiast. I'm currently study information management at `}
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
        {`. I have a deep passion for new technologies and love finding creative ways to solve complex challenges.`}
      </p>
      <div className="my-8">
        <BlogPosts />
      </div>
    </section>
  );
}
