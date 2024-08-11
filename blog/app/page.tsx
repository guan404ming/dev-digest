import { BlogPosts } from "app/components/posts";

export default function Page() {
  return (
    <section>
      <h1 className="mb-8 text-2xl font-semibold tracking-tighter">
        My Blog
      </h1>
      <p className="mb-4">
        {`I'm Guan-Ming Chiu, an Information Management student at National Taiwan University. 
          I have a deep passion for new technologies and love finding creative ways to solve complex challenges. 
          I'm always excited to learn and innovate in the ever-evolving world of technology.`}
      </p>
      <div className="my-8">
        <BlogPosts />
      </div>
    </section>
  );
}
